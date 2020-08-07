# Area de importaciones de librerias
from django.contrib import admin
from .models import Cliente


# Registro del modelo Cliente 
admin.site.register(Cliente)