
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
        