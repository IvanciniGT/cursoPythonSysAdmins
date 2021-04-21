lista=(1,2,3,4,5,6,7,8,9,10)
texto="murcielago"

# Cuantos elementos tiene mi lista?
print( len(lista) )
print( len(texto) )

# Sacar un elemento concreto
print( lista[3] ) # Saca el cuarto elemento de la lista
print( texto[3] ) # Saca el cuarto elemento de la lista

print( lista[-3] ) # Saca el antepenultimo elemento de la lista
print( texto[-1] ) # Saca el ultimo elemento de la lista

print( texto[2:6] ) 
print( texto[2:-2] ) 
print( texto[:-2] ) 
print( texto[-2:] ) 
print( texto[3:] ) 

print(  (1,2,3) + (4,5,6)   )
print(  "hola" + "amigo"    )

print(  (1,2,3) * 4   )
print(  "hola"  * 4   )


lista=[1,2,3,4]
texto="Hola" # Es como si fueran TUPLAS
tupla=(1,2,3,4)

#texto[1]="a"
lista[1]=10
#tupla[1]=10

#print(texto)
print(lista)
#print(tupla)

lista=lista+[20]
lista.append(30)
print(lista)


tupla=("a","b","c")
lista=["a","b","c"]
diccionario={"valor1": "a","valor2": "b","valor3": "c"}

print(diccionario["valor2"])

lista_puertos_oracle=[1521,999]
lista_puertos_ssh=[22]
servicios={"tnslsnr": lista_puertos_oracle, "ssh": lista_puertos_ssh}

lista= {  "tnslsnr": [1521,999],   "ssh": [22] }
print(lista["tnslsnr"])

# Una lista es una estructura cómoda, cuando queremos hacer que cosas?
    # Almacenar un conjunto de datos que quiero procesar de arriba a abajo
        # Lista de la compra: Voy a comprar todos y cada uno 
        # de los elementos que tengo el la lista
        # Lista de tareas
# En una tabla
    # Almacenar un conjunto de datos que no quiero procesar de arriba a abajo a priori
        # Quiero poder rápidamente identificar los datos de uno que tenga almacenado
