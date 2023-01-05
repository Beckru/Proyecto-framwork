from django import forms

class regis(forms.Form):
    first_name=forms.CharField(label= 'Nombre', max_length=150)
    last_name=forms.CharField(label= 'Apellido', max_length=150)
    email = forms.EmailField(label="Email ") 
    password= forms.CharField(max_length=20)

class logi(forms.Form):
    email = forms.CharField(label="Email ",max_length=150)
    password = forms.CharField(label="Contraseña",max_length=20)

class publi(forms.Form):
    name=forms.CharField(label="Titulo",max_length=25)
    text=forms.CharField(label="texto", widget=forms.Textarea)
    date=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    image=forms.ImageField()
    user=forms.CharField(widget=forms.HiddenInput)




