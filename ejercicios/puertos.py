import subprocess  # For executing a shell command

def comprobarPuerto(host, puerto):
    comando = ['nc', '-vz', host, str(puerto)]
    codigo_salida=subprocess.call(comando)
    return codigo_salida==0

def comprobacionPuertos(servidor):
    for ip in servidor.ips:
        for estado_servicio in servidor.estados_de_servicios:
            for puerto in estado_servicio.servicio.puertos:
                comprobacion_correcta=comprobarPuerto(ip,puerto)
                if not comprobacion_correcta:
                    estado_servicio.estado=False
                    print(
                        "No he podido acceder al servicio: %s, en su puerto: %d, para la IP: %s" 
                            % (estado_servicio.servicio.nombre, puerto, ip) 
                        )
                else: 
                    estado_servicio.estado=True
