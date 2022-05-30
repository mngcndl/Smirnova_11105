import socket

sock = socket.socket()
sock.connect(('localhost', 1000))

life_balance = 3

while True:
    msg_from_server = sock.recv(1024).decode('utf-8')
    print()
    print(msg_from_server)
    if msg_from_server == 'Your opponent is typing a word, wait a little bit, please!':
        continue
    else:
        if msg_from_server.lower().count('game') == 0:
            if msg_from_server.count('Wasted life. Be careful, the last letter now is ') > 0:
                life_balance -= 1
                print('Life balance now is ' + str(life_balance) + '.')
            print('Type your word:')
            msg_to_server = str(life_balance) + input()
            sock.send(msg_to_server.encode('utf-8'))
        else:
            break
sock.close()
