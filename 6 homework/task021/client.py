import socket

sock = socket.socket()
sock.connect(('localhost', 1000))
while True:
    msg_from_server = sock.recv(1024).decode('utf-8')
    print(msg_from_server)
    if msg_from_server.count('dead') == 0 and msg_from_server.count('ank') == 0:
        sock.send(input().encode('utf-8'))
    else:
        break
sock.close()

#print(msg_from_server.decode('utf-8'))