#!/bin/python3

# Escribir en un fichero
import time

mario="Hola amigo\n"
gerardo="Como estás\n"


canal_al_archivo=open("ejemplo_fichero.txt","w")
canal_al_archivo.writelines([mario,gerardo])
canal_al_archivo.close()

with open('nuevo_fichero.txt', 'w') as canal_al_nuevo_fichero:
    canal_al_nuevo_fichero.write("NUEVO FICHERO")

# Escribir em un fichero
# Modo w: Borra el archivo y lo sustituye por lo que le pase        >
# Modo a: Añade al final del archivo lo que le pase                 >>
# Modo x: Es igual que el W, pero... si el fichero existe da un error

def escribir(texto,archivo):
    canal_al_archivo=open(archivo,"a")
    canal_al_archivo.write(texto)
    canal_al_archivo.close()
    
escribir("Hola amigo","ejemplo_fichero.txt")
escribir("Como estás??","ejemplo_fichero.txt")


#######
# Ventajas:
#   Pocas lecturas a disco
# Inconvenientes:
#   Necesito más RAM
canal_al_archivo=open("ejemplo_fichero.txt","r")
texto=canal_al_archivo.read()
canal_al_archivo.close()

for caracter in texto:
    print(caracter)

for linea in texto.split("\n"):
    print(">>>>>>"+linea)


#####
canal_al_archivo=open("ejemplo_fichero.txt","r")
for linea in canal_al_archivo:
    print(">>"+linea.rstrip()+"<<")
    print(">>"+linea[:-1]+"<<")

canal_al_archivo.close()

print("-"*80)


# Ventajas:
#   Necesito menos RAM
# Inconvenientes:
#   Más lecturas a disco
canal_al_archivo=open("ejemplo_fichero.txt","r")
while True:
    linea=canal_al_archivo.readline()
    if len(linea)==0:
        break
    print("___"+linea)

canal_al_archivo.close()


#############################


import os

print(os.path.exists("ejemplo_fichero.txt"))
print(os.path.exists("ejemplo_fichero.txtt"))

os.mkdir("/home/ubuntu/environment/prueba")
#os.rmdir("prueba")
os.remove("ejemplo_fichero.txt")

