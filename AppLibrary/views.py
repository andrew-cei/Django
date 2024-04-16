from django.shortcuts import render
from django.http import HttpResponse
from AppLibrary.models import *
from AppLibrary.forms import *

# Create your views here.
def inicio(request):
    return render(request, 'AppLibrary/inicio.html')

def usuarios(request):
    # Muestra los usuarios buscados
    if request.method == 'GET' and 'nombre' in request.GET:
        usuarioFormulario = UsuarioFormulario()
        nombre = request.GET['nombre']
        usuarios = Usuario.objects.filter(nombre__icontains=nombre)
        print('Entró al if: ', usuarios)
        return render(request, 'AppLibrary/usuarios.html', {'usuarioFormulario':usuarioFormulario, 'usuarios': usuarios, 'nombre':nombre})
    # Añade un usuario a la base de datos
    elif request.method == 'POST':
        # Lectura de datos enviados por formulario
        usuarioFormulario = UsuarioFormulario(request.POST)
        print(usuarioFormulario)
        if usuarioFormulario.is_valid:
            informacion = usuarioFormulario.cleaned_data
            usuario = Usuario(
                nombre = informacion['nombre'],
                apellido = informacion['apellido'],
                email = informacion['email'],
            )
            usuario.save()
            usuarioFormulario = UsuarioFormulario()
            return render(request, 'AppLibrary/usuarios.html',{'usuarioFormulario': usuarioFormulario})
    else:
        # Página original
        usuarioFormulario = UsuarioFormulario()
        return render(request, 'AppLibrary/usuarios.html', {'usuarioFormulario': usuarioFormulario})

def libros(request):
    # Muestra los libros buscados
    if request.method == 'GET' and 'titulo' in request.GET:
        libroFormulario = LibroFormulario()
        titulo = request.GET['titulo']
        libros = Libro.objects.filter(titulo__icontains=titulo)
        return render(request, 'AppLibrary/libros.html', {'libroFormulario':libroFormulario, 'libros': libros, 'titulo':titulo})
    # Añade un libro a la base de datos
    elif request.method == 'POST':
        # Lectura de datos enviados por formulario
        libroFormulario = LibroFormulario(request.POST)
        print(libroFormulario)
        if libroFormulario.is_valid:
            informacion = libroFormulario.cleaned_data
            libro = Libro(
                titulo = informacion['titulo'],
                autor = informacion['autor'],
                editorial = informacion['editorial'],
                codigo = informacion['codigo'],
            )
            libro.save()
            libroFormulario = LibroFormulario()
            return render(request, 'AppLibrary/libros.html',{'libroFormulario': libroFormulario})
    else:
        # Página original
        libroFormulario = LibroFormulario()
        return render(request, 'AppLibrary/libros.html', {'libroFormulario': libroFormulario})    

def albumes(request):
    # Muestra los albumes buscados
    if request.method == 'GET' and 'titulo' in request.GET:
        albumFormulario = AlbumFormulario()
        titulo = request.GET['titulo']
        albumes = Album.objects.filter(titulo__icontains=titulo)
        return render(request, 'AppLibrary/albumes.html', {'albumFormulario':albumFormulario, 'albumes': albumes, 'titulo':titulo})
    # Añade un album a la base de datos
    elif request.method == 'POST':
        # Lectura de datos enviados por formulario
        albumFormulario = AlbumFormulario(request.POST)
        print(albumFormulario)
        if albumFormulario.is_valid:
            informacion = albumFormulario.cleaned_data
            album = Album(
                titulo = informacion['titulo'],
                artistas = informacion['artistas'],
                disquera = informacion['disquera'],
                codigo = informacion['codigo'],
            )
            album.save()
            albumFormulario = AlbumFormulario()
            return render(request, 'AppLibrary/albumes.html',{'albumFormulario': albumFormulario})
    else:
        # Página original
        albumFormulario = AlbumFormulario()
        return render(request, 'AppLibrary/albumes.html', {'albumFormulario': albumFormulario})