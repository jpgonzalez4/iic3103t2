from django.conf.urls import url
from django.urls import path
from .views import HamburguesaRudView, IngredienteRudView, HamburguesaAPIView, IngredienteAPIView, HamburguesaIngredienteAddDestroyView

urlpatterns = [
    path('hamburguesa/<int:id>/', HamburguesaRudView.as_view(), name = 'hamburguesa-details'),
    path('hamburguesa/', HamburguesaAPIView.as_view(), name = 'hamburguesa-list'),
    path('ingrediente/<int:id>/', IngredienteRudView.as_view(), name = 'ingrediente-details'),
    path('ingrediente/', IngredienteAPIView.as_view(), name = 'ingrediente-list'),
    path('hamburguesa/<int:id>/ingrediente/<int:iid>/', HamburguesaIngredienteAddDestroyView.as_view(), name = 'hamburguesa-details'),
]
