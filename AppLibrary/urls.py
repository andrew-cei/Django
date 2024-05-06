from django.urls import path
from AppLibrary import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('albumes/', views.albumes, name='Albumes'),
    path('libros/', views.libros, name='Libros'),
    path('busqueda/', views.busqueda, name='Busqueda'),
    path('login/', views.login_request, name='Login'),
    path('registro/', views.register, name='Registro'),
    path('admin/', views.admin, name='Administración'),
    path('logout/', LogoutView.as_view(template_name='AppLibrary/logout.html'), name='Logout'),
    path('editarAlbum/', views.editar_album, name='EditarAlbumAdmin'),
    path('editarAlbum/<codigo_album>/', views.editar_album, name='EditarAlbumAdmin'),
    path('borrarAlbum/<codigo_album>/', views.borrar_album, name='BorrarAlbumAdmin'),    
    path('borrarLibro/<codigo_libro>/', views.borrar_libro, name='BorrarLibroAdmin'),
    path('editarPerfil/', views.editar_perfil, name='EditarPerfil'),
    path('albumes/lista', views.AlbumListView.as_view(), name='ListaAlbumes'),
    path('albumes/nuevo', views.AlbumCreateView.as_view(), name='NuevoAlbum'),
    path('albumes/<pk>', views.AlbumDetailView.as_view(), name='DetalleAlbum'),
    path('albumes/<pk>/editar', views.AlbumUpdateView.as_view(), name='EditarAlbum'),
    path('albumes/<pk>/borrar', views.AlbumDeleteView.as_view(), name='BorrarAlbum'),
    path('libros/lista', views.LibroListView.as_view(), name='ListaLibros'),
    path('libros/nuevo', views.LibroCreateView.as_view(), name='NuevoLibro'),
    path('libros/<pk>', views.LibroDetailView.as_view(), name='DetalleLibro'),
    path('libros/<pk>/editar', views.LibroUpdateView.as_view(), name='EditarLibro'),
    path('libros/<pk>/borrar', views.LibroDeleteView.as_view(), name='BorrarLibro'),    
    path('cambiarPass/', views.CambiarPass.as_view(), name='CambiarPass'),
    path('about/',views.about, name='About'),
]