from django.db import models


class Libro(models.Model):
    isbn = models.CharField(max_length=20, unique=True)
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    editorial = models.CharField(max_length=200, blank=True)
    anio_publicacion = models.IntegerField(null=True, blank=True)
    categoria = models.CharField(max_length=100, blank=True)
    num_paginas = models.IntegerField(null=True, blank=True)
    ubicacion = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=50, blank=True)
    copias_disponibles = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.titulo} ({self.isbn})"
