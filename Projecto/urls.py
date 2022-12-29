from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('registrarse/', views.registrarse),
    path('foro/',views.foro),
    path('login/',views.login)
]