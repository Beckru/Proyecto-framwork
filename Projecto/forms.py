from django import forms

class regis(forms.Form):
    first_name = forms.CharField(label="Nombre ", max_length=150)
    last_name = forms.CharField(label="Apellido", max_length=150)
    email = forms.CharField(label="Email ",max_length=150)
    password = forms.CharField(label="Contraseña",max_length=20)

class logi(forms.Form):
    email = forms.CharField(label="Email ",max_length=150)
    password = forms.CharField(label="Contraseña",max_length=20)