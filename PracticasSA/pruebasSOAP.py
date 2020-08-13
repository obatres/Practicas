from zeep import Client
from zeep import xsd
import http.client
import requests
from zeep.wsse.username import UsernameToken

#from auth0.v3.authentication import GetToken

from auth0 import v3
domain = 'api.softwareavanzado.world'
non_interactive_client_id = 'sa'
non_interactive_client_secret = 'fb5089840031449f1a4bf2c91c2bd2261d5b2f122bd8754ffe23be17b107b8eb103b441de3771745'

get_token = GetToken(domain)
token = get_token.client_credentials(non_interactive_client_id,
    non_interactive_client_secret, 'https://{}/api/v2/'.format(domain))
mgmt_api_token = token['access_token']




r = requests.get('https://api.softwareavanzado.world/index.php?option=com_contact&webserviceVersion=1.0.0&webserviceClient=administrator&filter[search]=201212734', auth=('sa','usac'))
#print(r.content)

#r = requests.post('https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=hal',data={'name':'cliente prueba'}, auth=('sa','usac'))
#print(r.status_code)+

r = requests.post("https://api.softwareavanzado.world/index.php?option=token&api=oauth2&grant_type=client_credentials&client_id=sa&client_secret=fb5089840031449f1a4bf2c91c2bd2261d5b2f122bd8754ffe23be17b107b8eb103b441de3771745")

#print(r.content)
#cliente  = Client('https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=soap&wsdl',wsse=UsernameToken('sa','usac'))


#print(cliente.service.readList())

#print (cliente.service.create("cliente prueba"))
header = xsd.Element(
    '{https://api.softwareavanzado.world/}auth',
    xsd.ComplexType([
        xsd.Element('{https://api.softwareavanzado.world/}username',xsd.String()),
        xsd.Element('{https://api.softwareavanzado.world/}password',xsd.String()),
    ])
)

header_value = header(username='sa', password='usac')
#print (cliente.service.readList(_soapheaders=[header_value]))

