from zeep import Client
from zeep import xsd


cliente  = Client(wsdl='https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=soap&wsdl')

print(cliente)

#print (cliente.service.readList())
header = xsd.Element(
    '{https://api.softwareavanzado.world/}auth',
    xsd.ComplexType([
        xsd.Element(
            '{https://api.softwareavanzado.world/}username',
            xsd.String()),
    ])
)