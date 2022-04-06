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


def multipliers_of_n_till_9(n):
    i = 2
    multipliers = {1}
    if n != 1:
        last = 1
        while i < n // 2 and last <= 9:
            if n % i == 0:
                if i < 9:
                    multipliers.add(i)
                if n // i < 9:
                    multipliers.add(n // i)
                last = i
            i += 1
    return multipliers


def nums_before_n_that_are_prime_and_in_n_generator(n):
    list_of_digits = list(set(list(str(n))))
    if list_of_digits.count('0') > 0:
        list_of_digits.__delitem__('0')
    for i in range(1, n):
        flag = True
        for j in range(len(list_of_digits)):
            if i % int(list_of_digits[j]) != 0:
                flag = False
                break
        if flag:
            yield i


deg_gen = deg_generator(15)
for i in range(10):
    print(next(deg_gen))

print('\n' + 'next generator')

even_gen = even_generator(-9182.10238978768)
while True:
    try:
        print(next(even_gen))
    except StopIteration:
        print('these are all even digits in this number')
        break

print('\n' + 'next generator')

prime_gen = prime_before_n_generator(103)
while True:
    try:
        print(next(prime_gen))
    except StopIteration:
        print('these are all prime numbers between 0 and this number')
        break

print('\n' + 'next generator')

last_gen = nums_before_n_that_are_prime_and_in_n_generator(185)
while True:
    try:
        print(next(last_gen))
    except StopIteration:
        print('these are all prime numbers that you were looking for')
        break
