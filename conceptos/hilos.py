# Programa que cuente (Nombre, cantidad)
# Soy el programa: Nombre, voy por el numero: 1
# Soy el programa: Nombre, voy por el numero: 2
# Soy el programa: Nombre, voy por el numero: 3

import time
from threading import Thread

class Contador(Thread):
    
    def __init__(self, nombre, cantidad, delay):
        super().__init__()
        self.nombre=nombre
        self.cantidad=cantidad
        self.delay=delay
        self.debo_contar=False
    
    def cuenta(self):
        self.debo_contar=True
        self.start()  
        
    def run(self): 
#        for actual in range(1,self.cantidad+1):
#            if self.debo_contar==False:
#                return
#            print ("Soy %s, voy por el %d" % (self.nombre,actual))
#            time.sleep(self.delay) # El hilo que está ejecutando este trabajo

        actual=0
        while actual<= self.cantidad and self.debo_contar:
            actual+=1
            print ("Soy %s, voy por el %d" % (self.nombre,actual))
            time.sleep(self.delay) # El hilo que está ejecutando este trabajo


    def deja_de_contar(self):
        self.debo_contar=False

    
mi_contador_1=Contador("Gerardo",30,1)
mi_contador_2=Contador("David",20,2)
mi_contador_3=Contador("Ferran",10,3)


mi_contador_1.cuenta()
mi_contador_2.cuenta()
mi_contador_3.cuenta()

# Una vez empiecen a contar, a los 5 segundos, paro el 1
time.sleep(5)
mi_contador_1.deja_de_contar()
# A los 15 segundos, el siguiente,
time.sleep(10)
mi_contador_2.deja_de_contar()
# A los 20 segundos el ultimo
time.sleep(5)
mi_contador_3.deja_de_contar()
