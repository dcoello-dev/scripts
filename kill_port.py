import os
import sys


os.system(
    'sudo netstat -tulpn | grep $1 | awk 1{"print $7"} | awk -F "/" 1{"print $1"} > PID')
archivo = open("PID", "r")
contenido = archivo.read()
print "matando: "+contenido
os.system('sudo kill -9 '+contenido)
