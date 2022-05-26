# variant no 4

import socket

sock = socket.socket()
sock.bind(('localhost', 1000))
sock.listen(1)

eng_symbols = 'qwertyuiop[]asdfghjkl;zxcvbnm,.`'
rus_symbols = 'йцукенгшщзхъфывапролджэячсмитьбюё'
#letters_match_eng_to_rus = {}
letters_match_rus_to_eng = {}
for i in range(32):
    #letters_match_eng_to_rus[eng_symbols[i]] = rus_symbols[i]
    letters_match_rus_to_eng[rus_symbols[i]] = eng_symbols[i]
print(letters_match_rus_to_eng)

nums = [i for i in range(1, 33)]

conn, address = sock.accept()
print('connected: ', str(address))

letters_eng = [0 for _ in range(32)]
letters_rus = [0 for _ in range(32)]

all_sent_letters = ''
while True:
    msg_from_client = conn.recv(1024).decode('utf-8')
    all_sent_letters += msg_from_client
    amount_of_eng_mentions = str(all_sent_letters.count(msg_from_client))
    if rus_symbols.count(msg_from_client) > 0:
        print('there')
        rus_analog = letters_match_rus_to_eng[msg_from_client]
        amount_of_rus_mentions = str(all_sent_letters.count(rus_analog))
        msg_to_client = msg_from_client + ' была прислана ' + amount_of_eng_mentions + ' раз(а), ' + rus_analog + \
                        ' была прислана ' + amount_of_rus_mentions + ' раз(а), в сумме - '\
                        + str(int(amount_of_eng_mentions) + int(amount_of_rus_mentions)) + ' раз(а) '
    else:
        msg_to_client = msg_from_client + ' была прислана ' + amount_of_eng_mentions + ' раз(а)'
    conn.send(msg_to_client.encode('utf-8'))
