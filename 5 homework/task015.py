import re


def odd_a_some_c_even_b(lst):
    pattern = r'\ba(aa)*(ccc|c{5})*(bb)+\b'
    res = ''
    for st in lst:
        if re.search(pattern, st):
            if len(res) > 0:
                res += ', '
            res += st
    return res
