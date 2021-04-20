texto="Hola amigo!"
#      01234
# CASE
print( texto.upper() )          # Mayusculas
print( texto.lower() )          # Minusculas
print( texto.capitalize() )     # Primera letra en mayuscula el resto en minusculas
print( texto.title() )          # Primera letra de cada palabra mayuscula el resto en minusculas
print( texto.swapcase() )       # Cambiar el case

# Blancos (espacios, tabuladores, saltos de linea)
print( texto.isspace() ) # Esta funcion devuelve True o False. Devuelve True si TODOS los caracteres son blancos
print( texto[4].isspace() ) # Esta funcion devuelve True o False. Devuelve True si TODOS los caracteres son blancos

otro_texto="   Ivan    "
print(">>>"+otro_texto+"<<<")
print(">>>"+otro_texto.strip()+"<<<")
print(">>>"+otro_texto.lstrip()+"<<<")
print(">>>"+otro_texto.rstrip()+"<<<")

otro_texto_mas="En un lugar de la Mancha, de cuyo nombre no quiero acordarme..."
print(otro_texto_mas.split())
print(otro_texto_mas.split(','))


# Formatear textos

# print(  "FORMATO" % VALORES  )

valores=("Ivan", 42)
print( "Hola %-10s. Cuantos años tienes? Tengo %-2d años." % valores) 

valores=("Mariete", 4)
print( "Hola %-10s. Cuantos años tienes? Tengo %-2d años." % valores) 

