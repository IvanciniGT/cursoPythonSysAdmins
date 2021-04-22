import re

with open("apache.log") as logs:
    contenido=logs.read()

PATRON="(?<=[0-9]{3}\s)[0-9]+"
lista_bytes=re.findall(PATRON,contenido)

total_bytes=0

for cantidad_bytes in lista_bytes:
    total_bytes+=int(cantidad_bytes)

print("Total: %d MiB" % (total_bytes/1024/1024))



#1 Gibibyte antes eran 1024*1024*1024 bytes
#1 Mebibyte antes eran 1024*1024 bytes 
#1 Kibibyte antes eran 1024 bytes



#1 Gigabyte hoy en dia eran 1000*1000*1000 bytes
#1 Megabyte hoy en dia eran 1000*1000 bytes
#1 Kilobyte hoy en dia eran 1000 bytes