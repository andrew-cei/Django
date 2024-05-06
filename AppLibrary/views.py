from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from AppLibrary.models import *
from AppLibrary.forms import *

class CambiarPass(LoginRequiredMixin, PasswordChangeView):
    template_name = 'AppLibrary/cambiar_pass.html'
    success_url = reverse_lazy('EditarPerfil')

class AlbumListView(LoginRequiredMixin, ListView):
    model = Album
    context_object_name = 'albumes'
    template_name = 'AppLibrary/album_lista.html'

class AlbumDetailView(LoginRequiredMixin, DetailView):
    model = Album
    template_name = 'AppLibrary/album_detalle.html'

class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    template_name = 'AppLibrary/album_crear.html'
    success_url = reverse_lazy('ListaAlbumes')
    fields = ['titulo', 'artistas', 'disquera', 'anio', 'codigo']

class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    template_name = 'AppLibrary/album_editar.html'
    success_url = reverse_lazy('ListaAlbumes')
    fields = ['titulo', 'artistas', 'disquera', 'anio', 'codigo']

class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    template_name = 'AppLibrary/album_borrar.html'
    success_url = reverse_lazy('ListaAlbumes')

class LibroListView(LoginRequiredMixin, ListView):
    model = Libro
    context_object_name = 'libros'
    template_name = 'AppLibrary/libro_lista.html'

class LibroDetailView(LoginRequiredMixin, DetailView):
    model = Libro
    template_name = 'AppLibrary/libro_detalle.html'

class LibroCreateView(LoginRequiredMixin, CreateView):
    model = Libro
    template_name = 'AppLibrary/libro_crear.html'
    success_url = reverse_lazy('ListaLibros')
    fields = ['titulo', 'autor', 'editorial', 'anio', 'codigo']

class LibroUpdateView(LoginRequiredMixin, UpdateView):
    model = Libro
    template_name = 'AppLibrary/libro_editar.html'
    success_url = reverse_lazy('ListaLibros')
    fields = ['titulo', 'autor', 'editorial', 'anio', 'codigo']

class LibroDeleteView(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = 'AppLibrary/libro_borrar.html'
    success_url = reverse_lazy('ListaLibros')

# Create your views here.
def inicio(request):
    return render(request, 'AppLibrary/inicio.html')

def albumes(request):
    # Muestra los albumes buscados
    if request.method == 'GET' and 'titulo' in request.GET:
        albumFormulario = AlbumFormulario()
        titulo = request.GET['titulo']
        albumes = Album.objects.filter(titulo__icontains=titulo)
        return render(request, 'AppLibrary/busqueda.html', {'albumFormulario':albumFormulario, 'albumes': albumes, 'titulo':titulo})
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
        return render(request, 'AppLibrary/busqueda.html', {'albumFormulario': albumFormulario})

def libros(request):
    # Muestra los libros buscados
    if request.method == 'GET' and 'titulo' in request.GET:
        libroFormulario = LibroFormulario()
        titulo = request.GET['titulo']
        libros = Libro.objects.filter(titulo__icontains=titulo)
        return render(request, 'AppLibrary/busqueda.html', {'libroFormulario':libroFormulario, 'libros': libros, 'titulo':titulo})
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
        return render(request, 'AppLibrary/busqueda.html', {'libroFormulario': libroFormulario})
    
def busqueda(request):
    return render(request, 'AppLibrary/busqueda.html')
    
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        # Validación del formulario enviado
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            # Autenticación del usuario
            user = authenticate(username = usuario, password = contra)
            # Si está autenticado
            if user is not None:
                login(request, user)
                return render(request, 'AppLibrary/inicio.html', {'Mensaje':f'Bienvenido {usuario}'})
            # Si no está autenticado
            else:
                return render(request, 'AppLibrary/inicio.html', {'Mensaje': 'Datos incorrectos'})
        # Si no envió los datos de forma correcta
        else:
            return render(request, 'AppLibrary/inicio.html', {'Mensaje': 'Formulario erroneo'})
    form = AuthenticationForm()
    return render(request, 'AppLibrary/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'AppLibrary/inicio.html', {'menasje': 'Usuario creado'})
    else:
        form = UserRegisterForm()
    return render(request, 'AppLibrary/registro.html', {'form':form})

@login_required
def admin(request):
        print(request.user)
        libros = Libro.objects.all()
        albumes = Album.objects.all()
        return render(request, 'AppLibrary/administrador.html', {'libros': libros, 'albumes': albumes})

@login_required
def borrar_libro(request, codigo_libro):
    libro = Libro.objects.get(codigo = codigo_libro)
    libro.delete()
    # Página original
    return admin(request)

@login_required
def borrar_album(request, codigo_album):
    album = Album.objects.get(codigo = codigo_album)
    album.delete()
    # Página original
    return admin(request)

@login_required
def editar_album(request, codigo_album=None):
    if request.method == 'POST':
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
            return admin(request)
    else:
        album = Album.objects.get(codigo = codigo_album)
        albumFormulario = AlbumFormulario(initial={'titulo':album.titulo, 'artistas': album.artistas, 'disquera':album.disquera, 'anio':album.anio, 'codigo':album.codigo})
        return render(request, 'AppLibrary/administrador.html', {'albumFormulario':albumFormulario})

@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, instance=request.user)
        if miFormulario.is_valid():
            miFormulario.save()
            return render(request, 'AppLibrary/inicio.html')
    else:
        miFormulario = UserEditForm(instance=request.user)
        return render(request, 'AppLibrary/editar_perfil.html', {'miFormulario':miFormulario,'usuario':usuario})
    
def about(request):
    return render(request,'AppLibrary/about.html')