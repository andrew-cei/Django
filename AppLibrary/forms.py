from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class LibroFormulario(forms.Form):
    titulo = forms.CharField()
    autor = forms.CharField()
    editorial = forms.CharField()
    anio = forms.DateField()
    codigo = forms.IntegerField()

class AlbumFormulario(forms.Form):
    titulo = forms.CharField()
    artistas = forms.CharField()
    disquera = forms.CharField()
    anio = forms.DateField()
    codigo = forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)     
    normal_user = forms.BooleanField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2',  'normal_user'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
    password=None
    first_name = forms.CharField(label='Nombre')    
    last_name = forms.CharField(label='Apellido')
    email = forms.EmailField(label='Ingrese su email')    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']