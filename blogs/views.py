from django.shortcuts import render
from django.shortcuts import HttpResponse


def index(request):
    return render(request, "blogs/index.html")