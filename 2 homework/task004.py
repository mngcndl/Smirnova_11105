from functools import reduce


def word_composer(s, letter):
    return s + letter


a = input()
lst = []
word = ''
words_with_more_than_3_dif_letters = []
letters = set()

i = 0
while i != len(a) - 1:
    if a[i].isalpha():
        this_word = []
        while a[i].isalpha():
            this_word.append(a[i])
            letters.add(a[i])
            i += 1
        word = reduce(word_composer, this_word)
        lst.append(word)
        if len(letters) > 3:
            words_with_more_than_3_dif_letters.append(word)
    else:
        i += 1
        letters.clear()

if len(words_with_more_than_3_dif_letters) > 0:
    print('Here is a list of all words with more than 3 different letters:')
    print(words_with_more_than_3_dif_letters)
else:
    print('There are no any words with more than 3 different letters :(')

foo_words = list(filter(lambda x: x.count('foo') > 0, lst))
len_of_foo_words = 0
for i in range(len(foo_words)):
    len_of_foo_words += len(foo_words[i])

print('\n' + ''"Total length of words that contain \'foo\' is " + str(len_of_foo_words))
if len(foo_words) > 0:
    print('(these words are ' + ', '.join(foo_words) + ')')
