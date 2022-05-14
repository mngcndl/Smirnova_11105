import re


def a_in_n_degree_plus_any_letter_except_b(st):
    pattern = r"\ba+[^b]\b"
    return re.findall(pattern, st)
