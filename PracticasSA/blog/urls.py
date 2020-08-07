from django.urls import path
from . import views

urlpatterns = [
    # Url que dirige a la pagina principal de la aplicacion
    path('', views.client_list, name='client_list'),

    #Url que dirige a la pagina de Registro del cliente en la aplicacion
    path('Cliente/Registro', views.Registro, name='Registro'),
]