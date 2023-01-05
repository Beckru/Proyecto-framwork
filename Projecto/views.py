from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import regis, logi, publi
from.models import usuarios, publicacion
from django.contrib.sessions.backends.db import SessionStore
from django.contrib import sessions

#from .models import .... # aqui se ponen las tablas
# Create your views here.
def inicio(request):
    if request.session.get('email'):
        usua= request.session.get('email')
        print(usua)
    return render(request, 'inicio.html')

def registrarse(request):
    if request.method == 'GET':
        return render(request, 'registrarse.html',{
            'form': regis
        })
    else:
        usua=usuarios.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email= request.POST['email'],
            password= request.POST['password']
        )
        emai=request.POST['email']
        if emai.endswith('@estudiantesunap.cl'):
            usua.is_estudent= True
            usua.save()
        elif emai.endswith('@unap.cl'):
            usua.is_staff= True
            usua.save()
        else:
            print("XD")
        request.session['email']=emai
        return redirect('/')

def foro(request):
    return render(request, 'foro.html')

def logins(request):
    if request.method == 'GET':
        return render(request, 'login.html',{
        'form' : logi
        })

    else:
        #usuario =usuarios.objects.get(email= request.POST['email'])
        usuario =get_object_or_404(usuarios, email= request.POST['email'])
        if usuario:
            print("hola")
            return redirect('/foro/')

def crear_publicacion(request):
    email=request.session.get('email')
    user_b=usuarios.objects.get(email=email)
    user_a=str(user_b.id)
    if request.method == 'GET':
        return render(request, 'crear_publicacion.html', {
            'form' : publi
        })

    else:
        publicacion.objects.create(
            name=request.POST['name'],
            text=request.POST['text'],
            date=request.POST['date'],
            image=request.FILES['image'],
            user=user_b
            
        )
        return redirect('/foro/')
def foro(request):
    return render(request, 'foro.html')


    #return render(request, 'crear_publicacion.html',{
    #    'form' : publi
    #})