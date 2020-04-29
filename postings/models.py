from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.

class Ingrediente(models.Model):
    nombre        = models.CharField(max_length=255, null=True, blank=True)
    descripcion   = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.nombre)

class Hamburguesa(models.Model):
    nombre       = models.CharField(max_length=255, null=True, blank=True)
    precio       = models.PositiveIntegerField(null=True, blank=True)
    descripcion  = models.TextField(null=True, blank=True)
    imagen       = models.URLField(null=True, blank=True)   
    ingredientes = models.ManyToManyField(Ingrediente, blank=True)

    def __str__(self):
        return str(self.nombre)