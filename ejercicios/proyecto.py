import os
from servidores import cargar_servidores
from fabric import Connection
from jinja2 import Template

# Quiero un programa que:
# -----------------------
# Leer de una variable de entorno llamada: IMAGEN y de otra llamada VERSION
# los datos de una imagen de contenedor que vamos a descargar.
imagen=os.environ['IMAGEN']
version=os.environ['VERSION']
# Quiero leer de un fichero YAML, un listado de servidores (por ahora vais a poner solo el 172.17.0.2)
tabla_servidores=cargar_servidores()
# Y los quiero cargar esos servidores
#
# Acceder a cada servidor... que ahora solo tengo 1 via ssh

os.environ['use_ssh_config']="True"
os.environ['key_filename']="~/.ssh/id_rsa"

for servidor in tabla_servidores.values():
    conexion_ssh=Connection(host='root@'+servidor.ips[0])
    datos_del_servidor={ "IMAGEN": imagen, "VERSION": version }
    
    with open("docker-compose.yaml") as archivo_de_la_plantilla:
        texto_de_la_plantilla=archivo_de_la_plantilla.read()
        
    plantilla=Template(texto_de_la_plantilla)
    
    with open("archivo_a_copiar",'w') as archivo_configuracion:
        archivo_configuracion.write(plantilla.render(datos_del_servidor))
    
# Instalarle docker-compose
    conexion_ssh.put("archivo_a_copiar", remote="/root/docker-compose.yaml")
    conexion_ssh.run("apt install docker-compose docker -y")
# Crear un contenedor desde la imagen que me hayan dicho
    conexion_ssh.run("docker-compose up -d -f /root/docker-compose.yaml")
