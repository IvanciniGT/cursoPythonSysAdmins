
# Quiero una funcion que me devuelva el mayor de 2 numeros
def mayor(numero1,numero2):
    if numero1 > numero2:
        return numero1
    else:
        return numero2
    #return numero2 if numero2>numero1 else numero1
    
el_mayor=mayor(7,3)
print(el_mayor)

def mayor_de_tres(numero1,numero2,numero3):
    return mayor(mayor(numero1,numero2),numero3)

el_mayor=mayor_de_tres(7,3,11)
print(el_mayor)


# Quiero una funcion que calcule el factorial de un numero
# Factorial de 5=    5! = 5x4x3x2x1= 120
# ----------------------------------------
# Factorial de 5=    5! = 5 x 4!
# Factorial de 4=    4! = 4 x 3!
# Factorial de 3=    3! = 3 x 2!
# Factorial de 2=    2! = 2 x 1!
# Factorial de 1=    1! = 1 x 0!
# Factorial de 0=    0! = 1
# RECURSIVIDAD: Hago una función que se llama a si misma
def factorial(numero):
    #resultado=1
    #if numero>0:
    #    resultado=numero*factorial(numero-1)
    #return resultado

    if numero==0:
        return 1 # Por definición
    return numero*factorial(numero-1)

print(factorial(5))

# Factorial de 5=    5! = 5x4x3x2x1= 120
def factorialWhile(numero):
    resultado=numero
    while numero>1:
        numero-=1
        resultado*=numero
    return resultado

print(factorialWhile(5))

# Proceso en un SO?
# Un programa cargado en RAM en un estado compatible con EJECUCION
    # Puedo tener un proceso en EJECUCION
    # Puedo tener un proceso COLGADO (DEADLOCK)
    # Puedo tener un proceso TERMINADO
# Que es un hilo - Thread?
#   Un hilo es un trozo de código que se ejecuta dentro de un proceso de forma paralela a otros hilos
# Un proceso puede abrir muchos hilos de ejecución
# Cython? Solo puede tomar una CPU.
# Tiene sentido abrir hilos?
#   TODO EL DEL MUNDO:
#       Un hilo, no está solo usando CPU
#       Que puede hacer un hilo?
#           - Cálculos en una CPU
#           - Esperando la respuesta de un programa
#           - Leyendo del disco duro datos

# ¿Cómo se bare un hilo en la BASH?   
# Que abre un & en la bash ???  UN SUBPROCESO
# Siempre asociado a un hilo existe la llamada: PILA DE FUNCIONES
#                                               Functions stack                    



# Factorial de 5=    5! = 5x4x3x2x1= 120
def factorialFor(numero_original):
    resultado=numero_original
    for numero in range(1,numero_original):
        resultado*=numero
    return resultado

print(factorialFor(5))