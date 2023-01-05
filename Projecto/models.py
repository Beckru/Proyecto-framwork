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

    def __str__(self):
        return self.first_name

class publicacion(models.Model):
    name = models.CharField(max_length=25)
    text = models.CharField(max_length=300)
    date = models.DateField(default="")
    image = models.CharField(max_length=150)
    user = models.ForeignKey(usuarios, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.name