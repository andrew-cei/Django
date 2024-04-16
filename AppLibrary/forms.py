from django import forms

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class LibroFormulario(forms.Form):
    titulo = forms.CharField()
    autor = forms.CharField()
    editorial = forms.CharField()
    codigo = forms.IntegerField()

class AlbumFormulario(forms.Form):
    titulo = forms.CharField()
    artistas = forms.CharField()
    disquera = forms.CharField()
    codigo = forms.IntegerField()