# Вариант 3

def st_generator(st1, st2):
    i = 0
    symb_st_1 = 0
    symb_st_2 = 0
    while True:
        if i == 2:
            i = 0
        if i % 2 == 0:
            ans = st1[symb_st_1]
            symb_st_1 += 1
            if symb_st_1 == len(st1):
                symb_st_1 = 0
            yield ans
        else:
            ans = st2[symb_st_2]
            symb_st_2 += 1
            if symb_st_2 == len(st2):
                symb_st_2 = 0
            yield ans
        i += 1


this_gen = st_generator('summer', 'fall')
for i in this_gen:
    print(i)
