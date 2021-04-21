import yaml

class Servidor:
    
    def __init__(self, nombre, ips, servicios):
        self.nombre=nombre.lower()
        self.ips=ips
        self.estados_de_servicios=[]
        for servicio in servicios:
            self.estados_de_servicios.append(  EstadoDeServicio(self, servicio, False)  )

    def __str__(self):
        visualizacion= "Servidor: %s\n" % (self.nombre)
        visualizacion+="   > IPs: %s\n" % (self.ips)
        visualizacion+="   > Estado de los servicios:\n"
        for estado_servicio in self.estados_de_servicios:
            visualizacion+="      %s\n" % (estado_servicio) 
        return visualizacion
    
    def __repr__(self):
        return "\n"+self.__str__()

class EstadoDeServicio:
    
    def __init__(self, servidor, servicio, estado):
        self.servicio=servicio
        self.servidor=servidor
        self.estado=estado

    def __str__(self):
        visualizacion=  "%s\n" % (self.servicio)
        visualizacion+= "%s\n" % ("OK" if self.estado else "NOK")
        return visualizacion
 
class Servicio:
    
    def __init__(self, nombre, puertos):
        self.nombre=nombre
        self.puertos=puertos

    def __str__(self):
        return "Servicio: %s\n > Puertos: %s" % (self.nombre, self.puertos)



def cargar_servidores():
    # Leido el fichero YAML de servicios
    with open('servicios.yaml', 'r') as fichero_servicios:
        servicios=yaml.load(fichero_servicios, Loader=yaml.FullLoader)
    
    # CReado un listado de objetos de tipo SERVICIO
    tabla_servicios_cargados={}
    for nombre_servicio in servicios:
        puertos=servicios[nombre_servicio]
        tabla_servicios_cargados[nombre_servicio]=Servicio(nombre_servicio, puertos)
    
    # Leido el fichero YAML de servidores
    with open('servidores.yaml', 'r') as fichero_servidores:
        servidores=yaml.load(fichero_servidores, Loader=yaml.FullLoader)
    
    # Creado un listado de objetos de tipo SERVIDOR
    tabla_servidores_cargados={}
    for nombre_servidor in servidores:
        informacion_del_servidor=servidores[nombre_servidor]
        ips=informacion_del_servidor["ips"]
        nombres_servicios=informacion_del_servidor["servicios"]
        
        lista_servicios_del_servidor=[]
        for nombre_servicio in nombres_servicios:
            lista_servicios_del_servidor.append(tabla_servicios_cargados[nombre_servicio])
        
        tabla_servidores_cargados[nombre_servidor]=Servidor(nombre_servidor, ips, lista_servicios_del_servidor)
    return tabla_servidores_cargados
    
    