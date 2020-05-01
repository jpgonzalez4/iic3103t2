from rest_framework import generics, mixins, status
from postings.models import Hamburguesa, Ingrediente
from .serializers import HamburguesaSerializers, IngredienteSerializers
from rest_framework.exceptions import APIException
from rest_framework.response import Response

# Create your views here.
class HamburguesaRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field = 'id'
    serializer_class = HamburguesaSerializers
    
    def get_queryset(self):
        return Hamburguesa.objects.all()

class IngredienteRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field = 'id'
    serializer_class = IngredienteSerializers

    def get_queryset(self):
        return Ingrediente.objects.all()

class HamburguesaIngredienteAddDestroyView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field = 'id'
    serializer_class = HamburguesaSerializers

    def get_queryset(self):
        return Hamburguesa.objects.all()
    
    def put(self, request, *args, **kwargs):
        try:
            instance = Hamburguesa.objects.get(id=kwargs['id'])
        except:
            return Response(
                {"code": "400", "descripcion":'Id de hamburguesa inválido'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            instance_2 = Ingrediente.objects.get(id=kwargs['iid'])
        except:
            return Response(
                {"code": "404", "descripcion":'Ingrediente inexistente'},
                status=status.HTTP_404_NOT_FOUND
            )
        instance.ingredientes.add(instance_2)
        kwargs['put'] = '1'
        return self.update(request, *args, **kwargs)
            
    def delete(self, request, *args, **kwargs):
        try:
            instance = Hamburguesa.objects.get(id=kwargs['id'])
        except:
            return Response(
                {"code": "400", "descripcion":'Id de hamburguesa inválido'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            instance_2 = Ingrediente.objects.get(id=kwargs['iid'])
        except:
            return Response(
                {"code": "404", "descripcion":'Ingrediente inexistente'},
                status=status.HTTP_404_NOT_FOUND
            )
        instance.ingredientes.remove(instance_2)
        kwargs['delete'] = '1'
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        if 'delete' in kwargs:
            return Response(
                {"code": "200", "descripcion":'ingrediente retirado'},
                status=status.HTTP_200_OK
            )

        elif 'put' in kwargs:
            return Response(
                {"code": "201", "descripcion":'Ingrediente agregado'},
                status=status.HTTP_201_CREATED
            )

    def perform_update(self, serializer, **kwargs):
        serializer.save()

class HamburguesaAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    pass
    lookup_field = 'id'
    serializer_class = HamburguesaSerializers

    def get_queryset(self):
        return Hamburguesa.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"code": "201", "descripcion":'hamburguesa creada'},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"code": "400", "descripcion":'input invalido'},
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except:
            return Response(
                {"code": "400", "descripcion":'input invalido'},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def patch(self, request, *args, **kwargs):
        try:
            instance = Hamburguesa.objects.get(id=kwargs['id'])
        except:
            return Response(
                {"code": "404", "descripcion":'Hamburguesa inexistente'},
                status=status.HTTP_404_NOT_FOUND
            )
        return self.update(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            return Response(
                    {"code": "200", "descripcion":'operacion exitosa'},
                    status=status.HTTP_200_OK
                )
        except:
            return Response(
                {"code": "400", "descripcion":'Parámetros inválidos'},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def perform_update(self, serializer):
        serializer.save()

class IngredienteAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    pass
    lookup_field = 'id'
    serializer_class = IngredienteSerializers

    def get_queryset(self):
        return Ingrediente.objects.all()
    
    def perform_create(self, serializer):
        try:
            serializer.save()
            return Response(
                {"code": "201", "descripcion":'ingrediente creado'},
                status=status.HTTP_201_CREATED
            )
        except:
            return Response(
                {"code": "400", "descripcion":'input invalido'},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except:
            return Response(
                {"code": "404", "descripcion":'ingrediente inexistente'},
                status=status.HTTP_400_BAD_REQUEST
            )
    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except:
            return Response(
                {"code": "400", "descripcion":'input invalido'},
                status=status.HTTP_400_BAD_REQUEST
            )