from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Libro(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=30)
    codigo = models.IntegerField()

class Album(models.Model):
    titulo = models.CharField(max_length=30)
    artistas = models.CharField(max_length=50)
    disquera = models.CharField(max_length=30)
    codigo = models.IntegerField()