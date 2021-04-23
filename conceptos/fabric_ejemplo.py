import os

from fabric import Connection

#print(os.environ['PATH'])

os.environ['use_ssh_config']="True"
os.environ['key_filename']="~/.ssh/id_rsa"

conexion_ssh=Connection(host='root@172.17.0.3')
conexion_ssh.run("netstat -lnt")
conexion_ssh.put("archivo.configuracion", remote="/tmp")
conexion_ssh.run("ls -l /tmp")

