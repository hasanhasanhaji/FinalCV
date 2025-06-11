from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index_view(request):
    return HttpResponse("<H1> Home </h1>")


def contact_view(request):
    return HttpResponse("<H1> Contact </h1>")


def about_view(request):
    return HttpResponse("<H1> About </h1>")
