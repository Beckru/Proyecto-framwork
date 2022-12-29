from django.shortcuts import render
from django.http import HttpResponse
#from .models import .... # aqui se ponen las tablas
# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def registrarse(request):
    return render(request, 'registrarse.html')

def foro(request):
    return render(request, 'foro.html')

def login(request):
    return render(request, 'login.html')

def crear_publicacion(request):
    return render(request, 'crear_publicacion.html')