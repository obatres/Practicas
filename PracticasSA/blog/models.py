from django.db import models

# Create your models here.


# Modelo Cliente, que tiene como unico campo un nombre
class Cliente(models.Model):

    # Campo que corresponde al nombre del cliente, puede tener como maximo 200 caracteres 
    nombre_cliente = models.CharField(max_length=200)

    # Funcion que retorna el nombre del cliente    
    def __str__(self):
        return self.nombre_cliente