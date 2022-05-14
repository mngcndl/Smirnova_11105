from task017 import abbreviation
from task016 import correct_time
from task014 import a_in_n_degree_plus_any_letter_except_b
from task015 import odd_a_some_c_even_b

def test_014_a_in_n_degree_plus_any_letter_except_b():
    assert a_in_n_degree_plus_any_letter_except_b('aaaab aad') == ['aad']

def test_015_odd_a_some_c_even_b():
    assert odd_a_some_c_even_b(list('b a ab aaabbb aaacccbbbb aaaccccbbbb aaacccccbb aaaabb aaaaabb'.split()))\
           == 'aaacccbbbb, aaacccccbb, aaaaabb'

def test_016_correct_time():
    assert correct_time('221:23') is None

def test_017_abbreviation():
    assert abbreviation('33 собачки бежали ПО ПОЛЮ') == ['ПО ПОЛЮ']
    