from django.db import models

# Create your models here.

class usuarios(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    password= models.CharField(max_length=20)
    is_staff= models.BooleanField(default=False)
    is_estudent = models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)