from servidor import Servidor  
from servidor import Servicio  

from colorama import init
from termcolor import colored

from servidor import cargar_servidores
from tester import Tester
from ping import ping_servidor
from puertos import comprobacionPuertos

init() # Inicialización de la libreria Colorama

# PASO 1: Cargar servidores
tabla_servidores=cargar_servidores()

# Paso2: Crear pingeadores
testers=[]
for servidor in tabla_servidores.values():
    # Tester de monitorización de IPS
    tester=Tester(servidor, 3, ping_servidor)
    testers.append(tester)
    tester.testea()
    # Tester de monitorización de Servicios
    tester=Tester(servidor, 3, comprobacionPuertos)
    testers.append(tester)
    tester.testea()
    
# Paso 4.... esperar hasta el infinto o 
# hasta el usuario diga que ya no quiere seguir
input("Pulsa Enter para parar de monitorizar")
for tester in testers:
    tester.deja_de_testear()






















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
    """