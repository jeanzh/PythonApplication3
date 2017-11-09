import socket, threading

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('0.0.0.0',10001))
s.listen(2)

while True:
    print('waitting connection')
    sock,addr=s.accept()
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()

def tcplink(sock,addr):
    print('Accept new connection from %s:%s'%addr)
    sock.send(b'wellcome')
    while True:
        d=sock.recv(1024)
        if not d or d.decode('utf-8')=='exit':
            break
        sock.send(('hello %s'%d.decode('utf-8')).encode('utf-8'))

    sock.close()
    print('Connection from %s:%s closed'%addr)
