import socket

HOST = ''
PORT = 50001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print('conn', conn)
print('Connection', addr)
while True:
    data = conn.recv(1024)
    if not data:break
    conn.send(data)
conn.close()