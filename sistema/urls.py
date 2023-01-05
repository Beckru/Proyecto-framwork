from django.contrib import admin
from django.urls import path, include
from django.contrib import sessions


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Projecto.urls'))
]
