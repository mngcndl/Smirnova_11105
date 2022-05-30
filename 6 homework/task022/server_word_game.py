import extra_funcs as f
import socket

sock = socket.socket()
sock.bind(('localhost', 1000))
sock.listen(2)

conn1, address1 = sock.accept()
print('connected_1: ', str(address1))
conn2, address2 = sock.accept()
print('connected_2: ', str(address2))

set_of_words = set()
clients_active = f.who_starts_the_game(conn1, conn2)
conn = f.choose_connection(clients_active)
conn.send('You start!'.encode('utf-8'))
clients_active = f.shift_connections(clients_active)
conn = f.choose_connection(clients_active)
conn.send('Your opponent is typing a word, wait a little bit, please!'.encode('utf-8'))
clients_active = f.shift_connections(clients_active)

print()

last_letter = ''
while True:
    conn = f.choose_connection(clients_active)
    msg = conn.recv(1024).decode('utf-8')
    print(f.beautiful_connection_status(clients_active))
    print(msg)
    print()
    if msg[0] != '0':
        word = msg[1:]
        if f.word_is_unique(word, set_of_words) is False:
            conn.send('This word already had been used. Try another one.'.encode('utf-8'))
            continue
        elif f.last_letter_match(word, last_letter) is False:
            msg_to_client = 'Wasted life. Be careful, the last letter now is ' + last_letter + '.'
            if int(msg[0]) - 1 == 0:
                f.game_final(clients_active)
                break
            conn.send(msg_to_client.encode('utf-8'))
        else:
            last_letter = word[-1]
            set_of_words.add(word)
            print(set_of_words)
            clients_active = f.shift_connections(clients_active)
            print(f.beautiful_connection_status(clients_active))
            conn = f.choose_connection(clients_active)
            msg_to_client_with_a_word = 'Your opponent wrote the following word: ' + '\n' + word + '.'
            conn.send(msg_to_client_with_a_word.encode('utf-8'))
    else:
        f.game_final(clients_active)
        break
