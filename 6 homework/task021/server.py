import socket
from random import randint
import functions_for_word_repr_and_processing as funcs


sock = socket.socket()
sock.bind(('localhost', 1000))
sock.listen(1)

conn, address = sock.accept()
print('connected: ', str(address))

words = ['apple', 'chest', 'mud', 'employee', 'reaction', 'construction', 'platform', 'foundation', 'hospital',
         'product', 'revenue', 'understanding', 'philosophy', 'negotiation', 'injury', 'insurance', 'bonus',
         'professor', 'data', 'sample', 'description', 'meaning', 'anxiety', 'editor', 'sympathy', 'classroom',
         'phone', 'software', 'highway', 'analyst', 'outcome', 'decision', 'organization', 'property', 'clothes'
         'student', 'inspiration', 'chapter', 'music', 'recognition', 'society', 'speech', 'hair', 'hat']
word = words[randint(0, len(words) - 1)]
letter_statuses = funcs.all_letters_closed(word)
letter_positions = funcs.letter_positions_dict(word)
set_of_letters = funcs.word_to_set_of_letters(word)

start_msg = "Let\'s start the game! Your word is " + funcs.word_repr_for_client(word, letter_statuses, letter_positions)\
            + ". It contains " + str(len(word)) + " letters. Type the first letter, please!"
conn.send(start_msg.encode('utf-8'))
set_of_opened_letters = set()

fail_counter = 0
while fail_counter < 5:
    msg_from_client = conn.recv(1024).decode('utf-8').lower()
    if not msg_from_client:
        break
    if len(msg_from_client) > 1:
        msg_to_client = 'There should be only one letter! Try again.'
    else:
        if msg_from_client in set_of_opened_letters:
            msg_to_client = 'You\'ve already tried to open this letter. Try another one.'
        else:
            set_of_opened_letters.add(msg_from_client)
            if msg_from_client not in set_of_letters:
                fail_counter += 1
                msg_to_client = 'The word doesn\'t contain this letter.' + '\n' + funcs.reply_pictured_new(fail_counter)
            else:
                letter_statuses[msg_from_client] = True
                word_for_client = funcs.word_repr_for_client(word, letter_statuses, letter_positions)
                msg_to_client = 'Nice attempt! Since now word looks for you like that: ' + word_for_client
                if word_for_client.count('_') == 0:
                    msg_to_client += '\n' + 'You won! Congrats :)))))) And thank you for the game!'
                    conn.send(msg_to_client.encode('utf-8'))
                    break
        if fail_counter == 5:
            msg_to_client += '\n' + 'Thank you for the game! The word was \'' + word + '\'.'
    conn.send(msg_to_client.encode('utf-8'))
conn.close()
