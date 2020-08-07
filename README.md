# Practicas de Software Avanzado

> Cliente web tipo SOAP que consume de los web service que provee https://api.softwareavanzado.world/ por medio de un archivo wsdl, el cual puede registrar clientes y visualizar los clientes creados que contengan en el nombre el siguiente texto "201212734" el cual corresponde al carnet de estudiante del desarrollador.


Este es el incio de la puesta en practica de los conocimientos adquiridos en el curso de Software avanzado, de la carrera de ingenieria en sistemas de la unversidad de San Carlos de Guatemala. 

## Instalacion 

Descargar el instalador de python desde su sitio, dependiendo del sistema operativo.
https://www.python.org/downloads/

## Ejemplo de uso

Dentro del directorio Practicas/PracticasSA se encuentra el archivo Manage.py

correr la terminal de comandos del sistema operativo en este directorio y ejecutar el siguiente comando:

OS  X y Linux:
```sh
python manage.py runserver
```
Windows:
```sh
py manage.py runserver
```
y dirigirse a la url 127.0.0.1:8000/ en el navegador predeterminado de la computadora.

Se mostrara la pagina principal, que contiene a todos los clientes que contienen "201212734", y al final del listado se encuentra el acceso a la pagina de resgistro ubicado en la pagina principal con el texto "Registro", el cual despliega la pagina en donde se puede ingresar un nuevo cliente. 

## Historial de versiones
* 0.1.1
  * Primera realese
  * CAMBIO: Agregada la funcion de despliegue y registro de clientes
* 0.0.1
  * Trabajo en progreso
  * CAMBIO: Creado el sitio en Django
  
  
  
