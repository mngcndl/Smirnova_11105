from task016 import correct_time
from task017 import abbreviation

file = open(r"Tasks014-020.txt", encoding="utf-8", mode='r')
line = file.readline()

i = 1
while line:
    string_res016 = correct_time(line)
    string_res017 = abbreviation(line)
    if string_res016:
        print("RegEx \"correct_time\", string number: " + str(i))
        print(str(string_res016) + '\n')
    if string_res017:
        print("RegEx \"abbriveation\", string number: " + str(i))
        print(str(string_res017) + '\n')
    line = file.readline()
    i += 1

