a = input()
ans = ''
opers = ''         
opers_list = ("+", "-", "*", "/")
open_bracket = 0

for i in range(len(a)):
    if a[i] == ' ':
        continue
    else:
        if a[i].isalpha() or a[i].isnumeric():
            ans += a[i]
            if len(opers) != 0 and open_bracket == 0:
                ans += opers[::-1]
                opers = ''
        elif a[i] in opers_list:
            opers += a[i]
        elif a[i] == '(':
            open_bracket += 1
        else:
            ans += opers[::-1]
            opers = ''
            open_bracket -= 1
print(ans)
