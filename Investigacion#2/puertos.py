import socket #importamos el modulo socket

#Determinamos los valores por defecto del host y el puerto a comprobar
host = '127.0.0.1'
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
 s.connect((host, port))
 s.shutdown(2)
 print ("Conexion existo a ")
 print (host + " en el puerto: " + str(port))
except:
 print ("No se puede conecter a ")
 print (host + " en el puerto: " + str(port))
