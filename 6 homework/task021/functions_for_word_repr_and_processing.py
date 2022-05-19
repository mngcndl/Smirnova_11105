def word_to_set_of_letters(word: str):
    return set(word)


def all_letters_closed(word: str) -> dict:
    letter_opened = {}
    word_letters = word_to_set_of_letters(word)
    # Next code fulfills a dictionary (letter_opened) with letters from word and their state.
    # Now all of states are False - it is equal to a letter that is not opened by client).
    for letter in word_letters:
        if letter not in letter_opened:
            letter_opened[letter] = False
    return letter_opened


def letter_positions_dict(word: str) -> dict:
    letter_positions = {}
    for i in range(len(word)):
        cur_letter = word[i]
        positions_list = letter_positions.get(cur_letter)
        if positions_list:
            new_positions_list = positions_list
            new_positions_list.append(i)
        else:
            new_positions_list = [i]
        letter_positions.update({cur_letter: new_positions_list})
    return letter_positions


def lst_to_str(lst) -> str:
    st = ''
    for i in range(len(lst)):
        st += str(lst[i])
    return st


def word_repr_for_client(word: str, letters_statuses: dict, letters_positions: dict) -> str:
    # можно, конечно, убрать letters_positions из списка аргументов и вычислять его внутри функции,
    # но возможно в финальной реализации проще будет сделать это один раз внутри кода игры.
    repr_word = ['_' for _ in range(len(word))]
    letters = list(letters_statuses.keys())
    for i in range(len(letters)):
        tek_letter = letters[i]
        if letters_statuses[tek_letter] is True:
            for j in letters_positions[tek_letter]:
                repr_word[j] = tek_letter
    return lst_to_str(repr_word)

#  ( )       1
#   |        2
#  /|\       3
#  / \       4
# <   >      5


def reply_pictured_new(wrong_guess_number):
    if wrong_guess_number > 5:
        return "You\'re already dead, so sorry...."

    parts_of_a_guy = [" ( ) ", "  |  ", " /|\ ", " / \ ", "<   >"]
    answer = ''
    for i in range(wrong_guess_number):
        answer += parts_of_a_guy[i] + '\n'
    if wrong_guess_number == 5:
        answer += "You\'re dead now, so sorry...."
    else:
        answer += "You still have got a chance to win! Don\'t give up."
    return answer
