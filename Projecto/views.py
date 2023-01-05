from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import regis, logi
from.models import usuarios
#from .models import .... # aqui se ponen las tablas
# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def registrarse(request):
    if request.method == 'GET':
        return render(request, 'registrarse.html', {
            'form' : regis
        })

    else:
        usuarios.objects.create(first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=request.POST['password'])
        return redirect('/login/')
def foro(request):
    return render(request, 'foro.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html',{
        'form' : logi
        })

    else:
        #usuario =usuarios.objects.get(email= request.POST['email'])
        usuario =get_object_or_404(usuarios, email= request.POST['email'])
        print("hola")
        return redirect('/foro/')


def crear_publicacion(request):
    return render(request, 'crear_publicacion.html')