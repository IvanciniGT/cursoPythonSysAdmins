

def carta(saludo,cuerpo,despedida):
    return saludo() + cuerpo()+ despedida()


def saluda():
    return ("Hola\n")

def saludo_formal():
    return ("Estimado colega\n")

def premio():
    return ("Has ganado un premio\n")

def despedida():
    return ("Hasta pronto ")
    
print(carta(saluda,premio,despedida))
print(carta(saludo_formal,premio,despedida))
    