from threading import Thread
from random import randint
from time import sleep

words = []

alphabet = 'qwertyuiopasdfghjklzxcvbnm'


def new_word_generation():
    sleep(randint(0, 1))
    new_word = ''
    len_of_word = randint(3, 10)
    for i in range(len_of_word):
        new_word += alphabet[randint(0, len(alphabet) - 1)]
    words.append(new_word)
    return new_word


class Gamer(Thread):
    def __init__(self, my_words: list):
        super().__init__()
        self.my_words = my_words

    def is_there_a_word(self, gamers_variable_for_word):
        while gamers_variable_for_word == '':
            a_word = new_word_generation()
            self.my_words.append(a_word)

        for i in range(len(self.my_words)):
            if self.my_words[i][0] == gamers_variable_for_word[0]:
                return self.my_words[i]
        a_word = new_word_generation()
        self.my_words.append(a_word)
        while a_word[0] != gamers_variable_for_word[0]:
            a_word = new_word_generation()
            self.my_words.append(a_word)
        return a_word


word_for_gamer_1 = new_word_generation()
word_for_gamer_2 = ''
