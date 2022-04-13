import re


def abbreviation(st):
    pattern = r'\b[А-ЯA-Z]{2,}(?: ?[А-ЯA-Z]{2,})*\b'
    return re.findall(pattern, st)


file = open(r"Tasks014-020.txt", encoding="utf-8", mode='r')
line = file.readline()

while line:
    string_res = abbreviation(line)
    if string_res:
        print(string_res)
    line = file.readline()

