# Вариант 3

import re
st = '01 000010100011 1111 000101000101 0000 010010001001 0011 0010101 01001011'

# Начало - 2 нуля, конец - 2 единицы
pattern = r"0{2}\d*1{2}"
print(re.findall(pattern, st))

# Содержит подстроку '01'
pattern = r"\d*[0]{1}[1]{1}\d*"
print(re.findall(pattern, st))

# Содержит и '00', и '11'
pattern = r"\d*[0]{2}\d*[1]{2}\d*|\d*[1]{2}\d*[0]{2}\d*"
print(re.findall(pattern, st))