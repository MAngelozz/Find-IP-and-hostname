import sys
import socket
from unittest import result

objetivo = socket.gethostbyname(input ("Inserte la dirección IP"))

print("escaneando objetivo: "+ objetivo)

try:
    for port in range(1,150):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        resultado = s.connect_ex((objetivo, port))
        if resultado == 0:
            print("El puerto {} esta abierto" .format(port))
            s.close()

except:
            print ("/Saliendo...")
            sys.exit(0)