from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('Cliente/Registro', views.Registro, name='Registro'),
]