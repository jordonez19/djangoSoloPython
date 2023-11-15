from django.urls import path
from .views import generate_pdf

app_name = "thisfpdf"

urlpatterns = [
    path("", generate_pdf,),
]
