import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('10.15.0.200',10001))
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()