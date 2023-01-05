from django.urls import path
from . import views
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions import backends
from django.contrib import sessions

urlpatterns = [
    path('', views.inicio),
    path('registrarse/', views.registrarse),
    path('foro/',views.foro),
    path('login/',views.logins),
    path('crear_publicacion',views.crear_publicacion)
]