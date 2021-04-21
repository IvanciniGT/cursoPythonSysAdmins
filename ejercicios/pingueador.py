
import time
from threading import Thread
from ping import ping


class Pingueador(Thread):
    
    def __init__(self, servidor, delay):
        super().__init__()
        self.servidor=servidor
        self.delay=delay
        self.debo_pinguear=False
    
    def pinguea(self):
        self.debo_pinguear=True
        self.start()  
        
    def run(self): 
        while self.debo_pinguear:
            for ip in self.servidor.ips:
                ping_correcto=ping(ip)
                if not ping_correcto:
                    print(
                        "No he podido hacer ping al servidor: %s, en su IP: %s" 
                            % (self.servidor.nombre, ip) 
                        )

            time.sleep(self.delay) # El hilo que está ejecutando este trabajo


    def deja_de_pinguear(self):
        self.debo_pinguear=False
