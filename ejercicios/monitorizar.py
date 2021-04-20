from servidor import Servidor  
from servidor import Servicio  

from colorama import init
from termcolor import colored

import yaml

init() # Inicialización de la libreria Colorama

# Leido el fichero YAML de servicios
with open('servicios.yaml', 'r') as fichero_servicios:
    servicios=yaml.load(fichero_servicios, Loader=yaml.FullLoader)

# CReado un listado de objetos de tipo SERVICIO
lista_servicios_cargados=[]
for nombre_servicio in servicios:
    puertos=servicios[nombre_servicio]
    lista_servicios_cargados.append(Servicio(nombre_servicio, puertos))
    
# Leido el fichero YAML de servidores
with open('servidores.yaml', 'r') as fichero_servidores:
    servidores=yaml.load(fichero_servidores, Loader=yaml.FullLoader)
print(servidores)

# Creado un listado de objetos de tipo SERVIDOR
lista_servidores_cargados=[]
for nombre_servidor in servidores:
    informacion_del_servidor=servidores[nombre_servidor]
    ips=informacion_del_servidor["ips"]
    nombres_servicios=informacion_del_servidor["servicios"]
    
    nombres_servicios >>>> lista de SERVICIOS
    
    Necesito sacar los servicios de la lista de servicios cargados, 
    cuyo nombre de servicio sea igual a uno de los nombres de servicio
    que he leido para el servidor y que tengo dentro de la lista llamada nombres_servicios
    
    Servidor(nombre_servidor, ips, servicios)
    
"""

def mostrarEstadoDeLosServicios(servidor):
    print(servidor.nombre)
    for estado_de_servicio in servidor.estados_de_servicios:
        datos= (estado_de_servicio.servicio.nombre, 
                estado_de_servicio.servicio.puertos,
                colored("OK", 'green') if estado_de_servicio.estado else colored("NOK", 'red'))
        print("  %-10s %-10s: %s" % datos)







mostrarEstadoDeLosServicios(servidor_oracle_produccion_1)
mostrarEstadoDeLosServicios(servidor_oracle_produccion_2)
"""



Servidor <<< Algo, Ente , abstracto que tiene:
                Nombre,
                IPs
                Estados de servicios
¿Como creo un servidor?
    Pasando nombre, lista ips, lista de SERVICIOS


Nombre? texto
IPs     lista de ip
IP      texto compuesto por 4 numeros separadors por un punto
Estado de servicio <<<< Algo, ente
    Servidor
    Servicio
    Estado

Servidor? Ver pagina 1
Servicio? Ente  que tiene
    nombre <<< Ver pagina 2
    puertos <<< lista de puerto

puerto? numero
Estado? Si|No
    