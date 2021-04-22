# Patron
# Buscar dentro de un texto un patron

#TEXTO               PATRON              LO CONTIENE?        EMPIEZA POR?         ACABA POR?
#-------------------------------------------------------------------------------------------------------    
#HOLA AMIGO          AMIGO                   √                   X                   √
#HOLA AMIGO          hola                    x                   x                   x
#HOLA AMIGO          HOLA                    √                   √                   x
#HOLA AMIGO          H.LA                    √                   √                   x    
#HOLA AMIGO          [A-Z]                   √                   √                   √
#HOLA AMIGO          [HO]                    √                   √                   √
#HOLA AMIGO          HO                      √                   √                   √
#HOLA AMIGO          H[AEIOU]?LA             √                   √                   √


#Caracter .   Significa: CUALQUIER CARACTER . Es un comodin
#[secuencia de caracteres para elegir UNO]

#?     La secuencia anterior puede aparecer o no
#+     La secuencia anterior debe aparecer al menos una vez
#*     La secuencia anterior puede aparecer al menos una vez
#{n,m} La secuencia anterior debe aparecer entre n y m veces

#\s   Caracter blanco (espacio, tabulador, salto de linea)

#91 987 65 54     [0-9]+\s[0-9]+\s[0-9]+
#                        > 91 987 65
#                        >    987 65 54

#[12][0-9]{3,4}[a-c]
#  2   9999      a
#129999a
# 29999a




#(?<=[0-9]{3}\s)[0-9]+


import re

texto="HOLA AMIGO 1276"
PATRON="[0-9]+"
resultado=re.search(PATRON,texto)
print(resultado.string)
print(resultado.group())
print(resultado.span())

texto="HOLA AMIGO 1276"
PATRON="[A-Z]+"
resultado=re.findall(PATRON,texto)
for texto in resultado:
    print(texto)

texto="HOLA AMIGO COMO ESTAS"    
PATRON="[AEIOU]"
resultado=re.sub(PATRON,"O",texto)
print(resultado)



texto="+34 91  876-56/ 87"    
PATRON="[+ -/]+"
resultado=re.split(PATRON,texto)
print(resultado)









