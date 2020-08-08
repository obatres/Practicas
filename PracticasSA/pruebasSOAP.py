from zeep import Client
from zeep import xsd
import globus_sdk

cliente  = Client(wsdl='https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=soap&wsdl')

print(cliente)

#print (cliente.service.readList())
header = xsd.Element(
    '{https://api.softwareavanzado.world/}auth',
    xsd.ComplexType([
        xsd.Element('{https://api.softwareavanzado.world/}username',xsd.String()),
        xsd.Element('{https://api.softwareavanzado.world/}password',xsd.String()),
    ])
)

header_value = header(username='sa', password='usac')
print (cliente.service.readList(_soapheaders=[header_value]))

