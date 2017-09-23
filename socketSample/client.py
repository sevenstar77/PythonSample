import socket

HOST='127.0.0.1'
PORT = 50001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(b'start')
data = s.recv(1024)
s.close()
print('Recived :: ', repr(data))