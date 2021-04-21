from servidor import Servidor  
from servidor import Servicio  

from colorama import init
from termcolor import colored

from servidor import cargar_servidores
from pingueador import Pingueador

init() # Inicialización de la libreria Colorama



# PASO 1: Cargar servidores
tabla_servidores=cargar_servidores()

# Paso2: Crear pingeadores
pingueadores=[]
for servidor in tabla_servidores.values():
    pingo=Pingueador(servidor, 3)
    pingueadores.append(pingo)
    # Paso 3: Empezar los pings
    pingo.pinguea()
    
# Paso 4.... esperar hasta el infinto o 
# hasta el usuario diga que ya no quiere seguir
input("Pulsa Enter para parar de pinguear")
for pingo in pingueadores:
    pingo.deja_de_pinguear()






















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