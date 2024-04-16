from django.urls import path
from AppLibrary import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('usuarios/', views.usuarios, name='Usuarios'),
    path('libros/', views.libros, name='Libros'),
    path('albumes/', views.albumes, name='Álbumes'),
]