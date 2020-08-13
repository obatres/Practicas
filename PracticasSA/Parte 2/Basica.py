# Area de importacion de librerias
# Libreria para la autenticacion basica por medio de HTTP
from requests.auth import HTTPBasicAuth 
# Libreria que permite crear una sesion con el usuario y contraseña que nos dan acceso a los servicios
from requests import Session
# Libreria que transporta los datos de la sesion creada
from zeep.transports import Transport

# Instancia de una nueva sesion
session = Session()
# Aplicacion de credenciales a la sesion
session.auth = HTTPBasicAuth("sa","usac")
# Instancia del cliente con la autenticacion y el WSDL 
client = Client('https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=soap&wsdl',transport=Transport(session=session))

print(client.service.create("201212734 cliente 1 Basic"))
print(client.service.readList(0,201212734))