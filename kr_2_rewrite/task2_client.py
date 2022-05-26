import socket

sock = socket.socket()
sock.connect(('localhost', 1000))

while True:
    print('Type a letter to send:')
    sock.send(input().encode('utf-8'))
    msg_from_server = sock.recv(1024)
    print(msg_from_server.decode('utf-8'))