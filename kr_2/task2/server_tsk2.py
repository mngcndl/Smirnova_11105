import socket

sock = socket.socket()
sock.bind(('localhost', 1000))
sock.listen(2)

conn1, address1 = sock.accept()
print('connected: ', str(address1))
conn2, address2 = sock.accept()
print('connected: ', str(address2))

all_values = []
while True:
    msg1 = conn1.recv(1024).decode('utf-8')
    msg2 = conn2.recv(1024).decode('utf-8')
    print(msg1)
    print(msg2)
    if msg1 == 'get' and msg2 != 'get':
        if len(all_values) == 0:
            all_values = [msg2]
        else:
            all_values.append(msg2)
        conn2.send('added'.encode('utf-8'))
        conn1.send(str(all_values).encode('utf-8'))
    elif msg1 != 'get' and msg2 == 'get':
        if len(all_values) == 0:
            all_values = [msg1]
        else:
            all_values.append(msg1)
        conn1.send('added'.encode('utf-8'))
        conn2.send(str(all_values).encode('utf-8'))
    elif msg1 == 'get' and msg2 == 'get':
        conn1.send(str(all_values).encode('utf-8'))
        conn2.send(str(all_values).encode('utf-8'))
    else:
        all_values.append(msg1)
        all_values.append(msg2)
        conn1.send('added'.encode('utf-8'))
        conn2.send('added'.encode('utf-8'))
