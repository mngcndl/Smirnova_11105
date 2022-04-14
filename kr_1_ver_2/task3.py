def st_generator(st):
    i = -1
    while True:
        if i == len(st):
            i = -1
        if i == -1:
            ans = ''
        else:
            ans = st[0:(i + 1)]
        i += 1
        yield ans


the = st_generator('General Kenobi')
print(len('General Kenobi'))
for i in the:
    print(i)