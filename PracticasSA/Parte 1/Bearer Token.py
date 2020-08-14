# Area de importaciones de librerias 
# Libreria que permite manejar archivos Json
import json
# Libreria que permite realizar HTTP requests
import requests

# Variable url que contiene la ruta de autenticacion del token
url = "https://api.softwareavanzado.world/index.php?option=token&api=oauth2"

# Variable data que contiene las credenciales necesarias para accesar al token de autenticacion
data = {
    "client_id":"sa",
    "client_secret":"fb5089840031449f1a4bf2c91c2bd2261d5b2f122bd8754ffe23be17b107b8eb103b441de3771745",
    "grant_type":"client_credentials",
}

# Variable response que realiza una accion POST al servidor de servicios
response = requests.request("POST", url, data=data)

# Variable auth_token que contiene el token de acceso que provee la accion guardada en la variable response
auth_token=response.json().get("access_token")

# -----------------------------------------------------------------------------------------------------------
# -----------------------------     CREACION DE UN CONTACTO    ----------------------------------------------
# -----------------------------------------------------------------------------------------------------------

# Variable header que contiene los encabezados del HTTP request, en el cual se incluyen la atenticacion de tipo Bearer junto con el token de acceso
headers = {
    "Authorization":"Bearer "+auth_token,
}

# Variable url que contiene la ruta al servidor de servicios
url = 'https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=hal'

# Variable data que contiene la informacion del contacto a crear 
data = {
    "name":"201212734 Cliente 10 Bearer",
}

#Variable response  que realiza la accion POST en el servidor de servicios en el cual crea el nuevo contacto
response = requests.post(url,json=data,headers=headers)

# -----------------------------------------------------------------------------------------------------------
# ----------------------------------     LISTA DE CONTACTOS    ----------------------------------------------
# -----------------------------------------------------------------------------------------------------------
# Variable header que contiene los encabezados del HTTP request, en el cual se incluyen la atenticacion de tipo Bearer junto con el token de acceso
headers = {
    "Authorization":"Bearer "+auth_token,
}

# Variable url que contiene la ruta al servicio que accede a la lista de contactos creados y filtrados por el string "201212734"
url = 'https://api.softwareavanzado.world/administrator/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=hal&filter[search]=201212734'

# Variable response que obtiene los datos solicitados por medio de la accion GET al servidor de servicios
response = requests.get(url,headers=headers)

# Impresion de los contactos creados, filtrados por medio del string "201212734"
print(response.json())