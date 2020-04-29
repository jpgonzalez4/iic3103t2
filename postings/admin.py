from django.contrib import admin

# Register your models here.
from .models import Hamburguesa, Ingrediente

admin.site.register(Hamburguesa)
admin.site.register(Ingrediente)