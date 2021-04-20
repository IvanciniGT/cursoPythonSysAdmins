# Qué es un bucle?
# En un trozo de código que se ejecuta varias veces

# En python tenemos 2 grandes instrucciones para realizar un bucle
# WHILE
    # En un trozo de código que se mientras se cumple una condición
# FOR
    # En un trozo de código que se ejecuta sobre cada elemento de una "lista"

por_el_numero_que_voy=1
numero_al_que_tengo_que_llegar=10
while por_el_numero_que_voy<=numero_al_que_tengo_que_llegar:
    print(por_el_numero_que_voy)
    por_el_numero_que_voy+=1 #por_el_que_voy=por_el_que_voy+1

# LA estructura del while es identica a la del IF
# if VALOR_LOGICO:
#   codigo a ejecutar SI se cumple la condicion

# while VALOR_LOGICO:
#   codigo a ejecutar MIENTRAS se cumple la condicion

# Python: por_el_numero_que_voy
# Java:   porElNumeroQueVoy
# BASH:   POR_EL_NUMERO_QUE_VOY

# Bucles FOR:
# En un trozo de código que se ejecuta sobre cada elemento de una "lista"
#lista=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
#lista=range(1,21)
for elemento in range(1,21,2):
    print(elemento)


