a = list(input().split())

ans = ''
opers = ('+', '-', '*', '/')
vars = []

for i in range(len(a)):
    if a[i] in opers:
        var1 = str(vars.pop())
        if ans == '':
            var2 = str(vars.pop())
            ans = var2 + ' ' + a[i] + ' ' + var1
        else:
            if a[i] == '+' or a[i] == '-':
                ans = var1 + ' ' + a[i] + ' ' + '(' + ans + ')'
            else:
                ans = '(' + ans + ') ' + a[i] + ' ' + var1
    else:
        vars.append(str(a[i]))
print(ans)
