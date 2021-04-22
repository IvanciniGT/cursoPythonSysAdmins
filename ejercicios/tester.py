
import time
from threading import Thread

class Tester(Thread):
    
    def __init__(self, servidor, delay, funcion_test):
        super().__init__()
        self.servidor=servidor
        self.delay=delay
        self.funcion_test=funcion_test
        self.debo_testear=False
    
    def testea(self):
        self.debo_testear=True
        self.start()  
        
    def run(self): 
        while self.debo_testear:
            self.funcion_test(self.servidor)
            time.sleep(self.delay) # El hilo que está ejecutando este trabajo

    def deja_de_testear(self):
        self.debo_testear=False
