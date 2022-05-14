import re


def correct_time(st):
    ans = ''
    pattern = r'\b(((0[0-5])|(1\d)|(2[0-3])):[0-5]\d)\b'
    res_findall = re.findall(pattern, st)
    for i in range(len(res_findall)):
        ans += res_findall[i][0] + ' '
    if ans == '':
        ans = None
    return ans
