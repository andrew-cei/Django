from django.db import models

# Create your models here.
class Album(models.Model):
    titulo = models.CharField(max_length=30)
    artistas = models.CharField(max_length=50)
    disquera = models.CharField(max_length=30)
    anio = models.DateField()
    codigo = models.IntegerField()

    def __str__(self):
        return f"Título: {self.titulo} Artistas: {self.artistas}"

class Libro(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=30)
    anio = models.DateField()
    codigo = models.IntegerField()

    def __str__(self):
        return f"Título: {self.titulo} Autor: {self.autor}"