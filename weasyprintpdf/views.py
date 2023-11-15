from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML, CSS
from io import BytesIO
from PyPDF2 import PdfFileMerger


def generate_pdf_with_header_footer(request):
    sql = "SELECT * FROM `equipos` WHERE `id` = 1"

    # Generando datos para la tabla
    data_for_table = [f"Dato {i + 1}" for i in range(80)]
    razonSocial = "pepito perez"

    context = {
        "data_for_table": data_for_table,
        "razon-social": razonSocial,
        "data": sql,
    }

    # Obtener el template y renderizarlo con el contexto
    template = get_template("pdf.html")
    html_content = template.render(context)

    # Crear un objeto BytesIO para guardar el PDF generado
    pdf_file = BytesIO()

    # Generar el PDF utilizando WeasyPrint
    HTML(string=html_content).write_pdf(
        pdf_file,
        stylesheets=[CSS(string="")],
    )

    # Configurar la respuesta HTTP con el PDF generado
    response = HttpResponse(pdf_file.getvalue(), content_type="application/pdf")
    response["Content-Disposition"] = 'filename="pdf_con_header_y_footer.pdf"'

    return response


def pdfmerge(request):
    # Generar PDFs individuales a partir de diferentes plantillas
    pdfs_to_merge = []
    data_for_table = [f"Dato {i + 1}" for i in range(80)]

    templates = [
        "pdf.html",
        "pfds/equipos1.html",
        "pfds/equipos2.html",
        "pfds/notas.html",
        "pfds/proceso.html",
        "pfds/transcripcion.html",
    ]

    for template_name in templates:
        template = get_template(template_name)
        context = {
            "data_for_table": data_for_table,
            "some_data": "Some Data for Template",
        }

        html_content = template.render(context)

        pdf_file = BytesIO()
        HTML(string=html_content).write_pdf(
            pdf_file,
            stylesheets=[CSS(string="")],
        )
        pdfs_to_merge.append(pdf_file)

    # Combinar los archivos PDF generados
    merger = PdfFileMerger()

    for pdf in pdfs_to_merge:
        pdf.seek(0)
        merger.append(pdf)

    # Crear un objeto BytesIO para guardar el PDF final
    output_pdf = BytesIO()
    merger.write(output_pdf)

    # Configurar la respuesta HTTP con el PDF generado
    response = HttpResponse(output_pdf.getvalue(), content_type="application/pdf")
    response["Content-Disposition"] = 'filename="merged_pdf.pdf"'

    return response


def generate_pdf(request):
    template = get_template("temp_pdf/base.html")
    context = {"name": "Hello World"}

    html_template = template.render(context)

    pdf_file = BytesIO()
    HTML(string=html_template).write_pdf(pdf_file)

    response = HttpResponse(pdf_file.getvalue(), content_type="application/pdf")
    response["Content-Disposition"] = 'filename="cotizacion.pdf"'

    return response
