
class Servidor:
    
    def __init__(self, nombre, ips, servicios):
        self.nombre=nombre.lower()
        self.ips=ips
        self.estados_de_servicios=[]
        for servicio in servicios:
            self.estados_de_servicios.append(  EstadoDeServicio(self, servicio, False)  )
    

class EstadoDeServicio:
    
    def __init__(self, servidor, servicio, estado):
        self.servicio=servicio
        self.servidor=servidor
        self.estado=estado
 
class Servicio:
    
    def __init__(self, nombre, puertos):
        self.nombre=nombre
        self.puertos=puertos

#servicio_ssh = Servicio( 'ssh' , [22] )
#numero       = 4
#texto        = "hola"

#servicio_ssh.nombre
#servicio_ssh.puertos