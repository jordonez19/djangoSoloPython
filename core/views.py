from django.views.generic import View
from django.shortcuts import render, redirect

class Homeview(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, "home.html", context)