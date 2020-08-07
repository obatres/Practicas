# Area de importaciones de librerias 
from django import forms

from .models import Cliente

# Clase que contiene el formulario del cliente, con base en el modelo Cliente
class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('nombre_cliente',)
