from django.shortcuts import render, HttpResponse
from django.views import View


# Create your views here.
class BlogListView(View):
    def Blog(self, request, *args, **kwargs):
        context = {}
        return render(request, "blog.html", context)
