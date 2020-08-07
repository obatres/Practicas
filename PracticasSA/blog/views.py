# Area de importaciones de librerias 
from django.shortcuts import render
# Importacion del modelo Cliente
from .models import Cliente
# Importacion del formulario de Cliente
from .forms import ClienteForm
# Importacion de la libreria para redireccionar 
from django.shortcuts import redirect
# Importacion de la libreria para consumir el wsdl
from zeep import Client
# Import para realizar request al web service
import requests

# Instancia del cliente obtenido del WSDL de https://api.softwareavanzado.world/
client  = Client(wsdl="https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=soap&wsdl")
 
# Vista correspondiente a la pagina que muestra el listado de clientes
def client_list(request):
    # Request que filtra los clientes creados que contienen en el nombre el texto "201212734"
    req = requests.get('https://api.softwareavanzado.world/administrator/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=hal&filter[search]=201212734')
    # Variable tipo dict que recibe como valor por referencia el retorno de un archivo Json, filtrado por _embedded e item
    lista = req.json().get("_embedded").get("item")
    # Variable que inicia una instancia de la clase List y permanece vacio
    clientes = []
    
    # Cliclo que filtra cada item y muestra solo el name de cada uno
    for i in lista:
        clientes.append(i.get("name"))

    # Retorno a la vista que contiene el listado de los clientes
    return render(request,'blog/client_list.html',{'clientes':clientes})

# Vista correspondiente a la pagina en la que se registran los clientes 
def Registro(request):
    # Instancia de formulario creado con base al modelo Cliente 
    form = ClienteForm(request.POST)
    
    if form.is_valid():
        # Instancia del campo que contiene el nombre del cliente
        nombre = form.cleaned_data['nombre_cliente']
        
        # Verificacion de la creacion del cliente en el servicio web
        if client.service.create(nombre):
            # Redireccionamiento al la pantalla principal
            return redirect('/')
        else:
            form = ClienteForm()   
    else:
        form = ClienteForm()
    # Redireccionamiento a la pagina del Registro del cliente 
    return render(request,'blog/Registro.html',{'form':form})