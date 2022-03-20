def deg_generator(n):
    tek_value = 1
    while True:
        yield tek_value
        tek_value *= n
        

def even_generator(n):
    n = str(n)
    for i in range(len(n)):
        if n[i].isnumeric():
            if int(n[i]) % 2 == 0:
                st = n[i]
                yield st


def is_prime(n):
    flag = True
    i = 2
    n = int(n)
    while i < n // 2 and flag:
        if n % i == 0:
            flag = False
            break
        i += 1
    return flag


def prime_before_n_generator(n):
    if n <= 0:
        return 'Это число можно анализировать только по модулю, чего мы делать не будем'
    else:
        for i in range(n):
            if is_prime(i):
                yield i


def prime_digits_of_n_generator(n):
    n = str(n)
    for i in range(len(n)):
        if is_prime(int(n[i])) and int(n) % int(n[i]) == 0:
            yield n[i]


# def nums_before_n_with_prime_digs_from_n_generator(n):
#     lst = [1]
#     for i in range(len(str(n))):
#         if is_prime(str(n[i])):
#             lst.append(str(n[i]))
#     if len(lst) > 1:
#         for i in range(n):
#             for j in range(len(lst)):
#                 if i % lst[j] != 0:
#                     continue
#             yield i


deg_gen = deg_generator(15)
for i in range(10):
    print(next(deg_gen))

print('\n' + 'next generator' + '\n')

even_gen = even_generator(-9182.10238978768)
while True:
    try:
        print(next(even_gen))
    except StopIteration:
        print('these are all even digits in this number')
        break

print('\n' + 'next generator' + '\n')

prime_gen = prime_before_n_generator(103)
while True:
    try:
        print(next(prime_gen))
    except StopIteration:
        print('these are all prime numbers between 0 and this number')
        break
