from django.shortcuts import render
from django.http import HttpResponse
#from .models import .... # aqui se ponen las tablas
# Create your views here.

def inicio(request):
    return HttpResponse("inicio")

def about(request):
    return HttpResponse("about")