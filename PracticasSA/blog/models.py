from django.db import models

# Create your models here.


class Cliente(models.Model):

    nombre_cliente = models.CharField(max_length=200)

    def publicar (self, nombre):
        print("aqui se va a publicar en el SOAP")

        
    def __str__(self):
        return self.nombre_cliente