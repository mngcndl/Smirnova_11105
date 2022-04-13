import re

lst = list('b a ab aaabbb aaacccbbbb aaaccccbbbb aaacccccbb aaaabb aaaaabb'.split())
pattern = r'\ba(aa)*(ccc|c{5})*(bb)+\b'
print(lst)

res = ''
for st in lst:
    if re.search(pattern, st):
        if len(res) > 0:
            res += ', '
        res += st
print(res)
