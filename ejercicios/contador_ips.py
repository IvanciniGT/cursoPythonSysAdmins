# El resultado va a ser una TABLA
# IP         CANTIDAD

resultado={}

with open('apache.log') as fichero:
    for linea in fichero:
        ip=linea[:linea.index(' ')]
        cantidad=resultado.get(ip, 0) # Permite opcionalmente un segundo parametro... que seria el valor por defecto a devolver si la clave no esta presente
        resultado[ip]=cantidad+1
        
with open('cantidad.ip','w') as fichero:
    for ip in resultado:
        fichero.write( "%s=%d\n" % (ip,resultado[ip]) )