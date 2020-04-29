from rest_framework import generics, mixins
from postings.models import Hamburguesa, Ingrediente
from .serializers import HamburguesaSerializers, IngredienteSerializers
from rest_framework.exceptions import APIException

# Create your views here.
class HamburguesaRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field = 'id'
    serializer_class = HamburguesaSerializers
    
    def get_queryset(self):
        return Hamburguesa.objects.all()

class HamburguesaAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    pass
    lookup_field = 'id'
    serializer_class = HamburguesaSerializers

    def get_queryset(self):
        return Hamburguesa.objects.all()
    
    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class HamburguesaIngredienteAddDestroyView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field = 'id'
    serializer_class = HamburguesaSerializers

    def get_queryset(self):
        return Hamburguesa.objects.all()
    
    def put(self, request, *args, **kwargs):
        instance = Hamburguesa.objects.get(id=kwargs['id'])
        instance_2 = Ingrediente.objects.get(id=kwargs['iid'])
        instance.ingredientes.add(instance_2)
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        instance = Hamburguesa.objects.get(id=kwargs['id'])
        instance_2 = Ingrediente.objects.get(id=kwargs['iid'])
        instance.ingredientes.remove(instance_2)
        return self.update(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        serializer.save()

class IngredienteRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field = 'id'
    serializer_class = IngredienteSerializers

    def get_queryset(self):
        return Ingrediente.objects.all()

class IngredienteAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    pass
    lookup_field = 'id'
    serializer_class = IngredienteSerializers

    def get_queryset(self):
        return Ingrediente.objects.all()
    
    def perform_create(self, serializer):
        serializer.save()
    
    def delete(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)