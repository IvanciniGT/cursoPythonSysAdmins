# Jinja es una libreria para trabajar con plantillas

from jinja2 import Template

datos_del_servidor={"cpus": 7, "nombre_servidor": "miserv1.prod", "ips": ["192.168.1.1","99.99.99.99"], "sistema_operativo": "windows"}

with open("archivo.configuracion.plantilla") as archivo_de_la_plantilla:
    texto_de_la_plantilla=archivo_de_la_plantilla.read()
    
plantilla=Template(texto_de_la_plantilla)

with open("archivo.configuracion",'w') as archivo_configuracion:
    archivo_configuracion.write(plantilla.render(datos_del_servidor))