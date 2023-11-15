from django.urls import path
from .views import generate_pdf, generate_pdf_with_header_footer, pdfmerge

app_name = "weasyprintpdf"

urlpatterns = [
    path(
        "",
        generate_pdf,
    ),
    path(
        "pdf/",
        generate_pdf_with_header_footer,
    ),
    path(
        "pdfmerge/",
        pdfmerge,
    ),
]
