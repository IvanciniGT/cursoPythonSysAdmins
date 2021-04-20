#!/bin/python3

# Esto es un comentario.
# Todo lo que se escriba detras de un cuadradito, se ignora al ejecutarse

# En python no existe comentario en bloque
# Existe una chapuza que hacemos, que es poner un texto en varias lineas, 
# sin asignar a ninguna variable
# Esto nos simula un comentario en bloque.
"""
    Todo lo que haya aqui
    Aunque ocupe varias lineas
    Se considera un comentario
"""

# Comentar un codigo es importantisimo. 
# Comentar un codigo y Documentar.
#   Mision de comentar un codigo?       Explicar como lo hace
#   Mision de documentar un codigo?     Explicar que hace

# VARIABLE
# Que es una variable?
    # Un valor guardado
    # Una seccion de memoria a la cual le asigno un valor que puede ser 
    # dinamico... o un conjunto
    
    # Una variable es una REFERENCIA a algo que tengo guardado en la RAM del ordenador
    # Sistema operativo! ponme el numero 3 en la RAM
    # Sistema operativo! ponme el numero 3 en la RAM, y al lado pon un postit con la palabra "NUMERO"
    # Sistema operativo! ponme el texto "hola" en la RAM
    # Sistema operativo! ponme el texto "hola" en la RAM, y al lado pon un postit con la palabra "TEXTO"
    # El postit es nuestra variable. Lo que varia de una variable es DONDE PEGO EL POSTIT?
    
numero=3
    # Cuantas cosas ocurren en esta linea de codigo? 3 cosas
        # Cosa 1: Pon el numero 3 en la RAM... en algun sitio... me da igual donde
        # Cosa 2: Crea un postit nuevo con la palabra escrita "NUMERO"... Es decir, una variable
        # Cosa 3: Pega el postit, al lado del numero 3. Asocia la variable a ese numero 3.
        
numero=7
    # Cuantas cosas ocurren en esta linea de codigo? 2 cosas
        # Cosa 1: Pon el numero 7 en la RAM... en algun sitio... me da igual donde
            # En este momento en la RAM esta el 3 y el 7
        # Cosa 2: Pega el postit, al lado del numero 7. Asocia la variable a ese numero 7.
        # PREGUNTA: Quien referencia ahora al numero 3? NADIE...
            # Entonces python, que es muy majete (no como C, que es cabroncete) como ve 
            # que el 3 ya no hay nadie referenciandolo, y que por tanto, no tengo forma 
            # de recuperarlo nunca mas lo borra de la RAM

numero2=3

numero3=numero2
numero2=7

# VALORES
3   
3.1
"hola"
'adios'
"""
Esto es un texto
multilinea
"""
True
False

(1,2,3) # Tupla. No es editable
[1,2,3] # Lista. Es como una tupla, pero editable


# OPERADORES
# Operadores aplicables a numeros
3+1
3-2
-6
3*5
11/5  # Division exacta: 2.2
11//5 # Division entera: 2
11%5  # Resto de la division entera: 1
# Operadores aplicados a textos
"hola"+"amigo"  # concatenar
"hola"*3        # Repetir el texto n veces
# Operadores comparativos : 
# Que resultado producen ? Un valor logico: True(1) | False(0)
1==1
1!=3
1>3
1>=3
1<=3
1<3
# Operadores que se aplican a valores logicos  True | False
not True        # False
True and True   # True 
    # Y: devuelve True si ambos lados son True. En cualquier otro caso da False
True or True   # True 
    # O: devuelve True si algunos de los valores a los lados es True. 
    
# Operadores de asignacion
numero=3
numero+=3 # incrementar el numero en 3
numero-=3 # decrementar el numero en 3
numero*=3 # triplico el numero
numero/=3 # un tercio del numero
numero=numero/3 # un tercio del numero


# FUNCIONES
# Una funcion es un trozo de programa reutilizable.
# Las funciones tienen un cometido
print("hola")
print("hola"+"amigo")
print(("hola"+"amigo")*4)
#print "hola"
minumero=input("Dame un número: ")
#            VVVV
#minumero="3746287264"
print("el numero que has introducido es el : " +minumero)
#print("el numero que has introducido es el : " +76) Esto daría error

# Funciones de conversion de tipos:
int("32") # Convierte un texto en numero
bool("True") # Convierte un texto en numero
str(32)
str(True)

# Palabras especiales, con su propio significado
# Condicionales
#if VALOR_LOGICO :
    # Codigo que se ejecutará si el valor lógico es True

if True:
    print("Es verdad")
    print("Es verdad")

if 3>2:
#if True:
 print("Es mentira")
 print("Es mentira")

print("Te has enterado?")

resultado=3>2 # True
if resultado:
    print("Saco un texto")
else:
    print("Saco otro texto")


numero=14
resto_entre_tres=numero%3 # 2 | 1 | 0

if resto_entre_tres==0:
    print("El numero es divisible entre 3")
elif resto_entre_tres==1:
    print("El numero es casi divisible entre 3")
elif resto_entre_tres==2:
    print("El numero no es divisible entre 3, ni de coña!")
    

# YO PUEDO CREAR MIS PROPIAS FUNCIONES
#       Podría poner que argumentos requiere la funcion para ejecutarse
#          V    
def saluda( ):
    print("Hola !")
    
saluda()
saluda()
saluda()
saluda()

def saludoPersonalizado( persona, veces):
    print(("Hola "+persona+"!")*veces)

saludoPersonalizado("Ivan",5)

def doblar(numero):
    return numero*2
    
doble=doblar(8) # 16
print("El doble es: "+str(doble))
