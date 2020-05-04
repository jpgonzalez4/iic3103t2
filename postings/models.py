from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.

class Ingrediente(models.Model):
    nombre        = models.CharField(max_length=255)
    descripcion   = models.TextField()

    def __str__(self):
        return str(self.nombre)

class Hamburguesa(models.Model):
    nombre       = models.CharField(max_length=255, blank=True)
    precio       = models.PositiveIntegerField(blank=True)
    descripcion  = models.TextField(blank=True)
    imagen       = models.URLField(blank=True)   
    ingredientes = models.ManyToManyField(Ingrediente, blank=True)

    def __str__(self):
        return str(self.nombre)