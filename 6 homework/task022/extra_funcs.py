from random import randint


def last_letter_match(word, letter):
    if word[0] == letter or letter == '':
        return True
    return False


def word_is_unique(word, word_set):
    if word in word_set:
        return False
    return True


def shift_connections(connection_status: dict) -> dict:
    for key in connection_status.keys():
        if connection_status[key]:
            connection_status[key] = False
        else:
            connection_status[key] = True
    return connection_status


def beautiful_connection_status(connection_status):
    res = '{'
    i = 1
    for key in connection_status.keys():
        res += str(i) + ': ' + str(connection_status[key])
        if i == 1:
            res += ','
        i += 1
    res += '}'
    return res


def choose_connection(connection_status: dict):
    for key in connection_status:
        if connection_status[key]:
            return key


def game_final(connection_status: dict):
    for key in connection_status:
        if connection_status[key]:
            key.send('Game over.'.encode('utf-8'))
    shift_connections(connection_status)
    for key in connection_status:
        if connection_status[key]:
            key.send('The game has been ended, you are the winner, congrats!'.encode('utf-8'))
    return 'game has been ended'


def who_starts_the_game(connection_1, connection_2):
    who = randint(1, 2)
    if who == 1:
        connection_status = {connection_1: True, connection_2: False}
        print('First client starts.')
    else:
        connection_status = {connection_1: False, connection_2: True}
        print('Second client starts.')
    print(connection_status)
    return connection_status
