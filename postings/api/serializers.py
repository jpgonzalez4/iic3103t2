from rest_framework import serializers
from postings.models import Hamburguesa, Ingrediente
from django.urls import reverse

# Create your views here.

class IngredienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = [
            'id',
            'nombre',
            'descripcion',
        ]
        extra_kwargs = {
            'name': {'validators': []},
        }

    def get_queryset(self):
        return Ingrediente.objects.all()

class IngredienteSerializers2(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()
    class Meta:
        model = Ingrediente
        fields = [
            'path',
        ]
        extra_kwargs = {
            'name': {'validators': []},
        }

    def get_queryset(self):
        return Ingrediente.objects.all()
    
    def get_path(self, obj):
        return 'https://iic3103t2.herokuapp.com{}'.format(reverse('ingrediente-details', args=[obj.id]))

class HamburguesaSerializers(serializers.HyperlinkedModelSerializer):
    ingredientes = serializers.SerializerMethodField()

    class Meta:
        model = Hamburguesa
        fields = [
            'id',
            'nombre',
            'precio',
            'descripcion',
            'imagen',
            'ingredientes',
        ]
        depth = 1

    def get_queryset(self):
        return Hamburguesa.objects.all()

    def get_ingredientes(self, obj):
        query = Ingrediente.objects.filter(hamburguesa = obj)
        ingredientes_serializer = IngredienteSerializers2(query, many=True)
        return ingredientes_serializer.data

