# Tipos de VALORES que podemos escribir en python

# Tipos básicos
numero1=1
numero2=7
numero3=1000000
6.7
True
False

# Tipos compuestos / complejos
# No solamente almacenan un valor, sino que:
    # Pueden almacenar toda una coleccion de valores
    # Esos tipos compuestos, tienen sus propias funciones definidas, para ellos

# Programación orientada a objetos => Capacidad de un lenguaje para pernitirnos 
# definir nuestros propios tipos

# Servidor
#  Caracteristicas / Propiedades / Atributos
#       Hardware
#           - # CPUs
#           - RAM
#       Servicios que tiene y servicios que están corriendo
#       S.O.
#       IP(s)

def imprimirDatosBasicosDeServidor(nombre, descripcion, so, nucleos):
    print("Nombre: " +nombre)
    print(" Descripcion: "+descripcion)
    print(" SO: "+so)
    print(" Nucleos: "+str(nucleos))

nombre="bbdd1.prod.es"
descripcion="Servidor de Base de datos 1"
nucleos=4
ram=32
so="ubuntu"
servicios=("oracle","listener")
estado_de_los_servicios=(True,False)
ips=("192.168.18.32","127.0.0.1")

nombre2="bbdd2.prod.es"
descripcion2="Servidor de Base de datos 2"
nucleos2=6
ram2=64
so2="ubuntu"
servicios2=("oracle","listener")
estado_de_los_servicios2=(True,False)
ips2=("192.168.18.31","127.0.0.1")

imprimirDatosBasicosDeServidor(nombre, descripcion, so, nucleos)
imprimirDatosBasicosDeServidor(nombre2, descripcion2, so2, nucleos2)

#

class Servidor:
    # Siempre vamos a crear dentro una función que indica a python Cómo se crean objetos de este tipo
    # Constructor
    def __init__(self, nombre, descripcion, so):
        self.nombre=nombre.lower()
        self.descripcion=descripcion.capitalize()
        self.so=so
    
    def imprimirDatos(self):
        print("Nombre: " +self.nombre)
        print(" Descripcion: "+self.descripcion)
        print(" SO: "+self.so)
    
servidor1 = Servidor("webserver1.prod.es", "Servidor web de producción 1", "Ubuntu")
servidor2 = Servidor("WEBSERVER2.PROD.es", "Servidor WEB de producción 2", "CentOS")
servidor3 = Servidor("webserver3.prod.es", "Servidor web de producción 3", "RHEL")
servidor4 = Servidor("webserver4.prod.es", "Servidor web de producción 4", "Windows")

servidor1.imprimirDatos()
servidor2.imprimirDatos()
servidor3.imprimirDatos()
servidor4.imprimirDatos()
