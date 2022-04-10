import re

pattern = r"\ba+[^b]\b"
st = 'aaab aaaac aaad ae ad b aedaab '
print(st)
print(re.findall(pattern, st))  # ['aaaac', 'aaad', 'ae', 'ad']
