import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
#    param ='-c'
#    if platform.system().lower()=='windows' :
#        param = '-n'
    # Option for the number of packets as a function of
#    if platform.system().lower()=='windows' :
#        param = '-n'
#    else:
#        param ='-c'
    # Option for the number of packets as a function of
    parametro = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    comando = ['ping', parametro, '1', host]
    codigo_salida=subprocess.call(comando)
        # Hace una llamada SINCRONA al comando
        # Es decitr, se llama al comando, se espera a que termine.
        # Al terminar, devuelve el código de salida del comando.
    return codigo_salida==0

def ping_servidor(servidor):
    for ip in servidor.ips:
        ping_correcto=ping(ip)
        if not ping_correcto:
            print(
                "No he podido hacer ping al servidor: %s, en su IP: %s" 
                    % (servidor.nombre, ip) 
                )
