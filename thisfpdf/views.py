from fpdf import FPDF
from django.http import HttpResponse
from io import BytesIO
from datetime import datetime


def generate_pdf(request):

    response = HttpResponse("application/pdf")
    return response
