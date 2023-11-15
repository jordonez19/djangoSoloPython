from django.urls import path
from .views import BlogListView

app_name = "blog"

urlpatterns = [
    path("inicio/", BlogListView.as_view(), name="home"),
]
