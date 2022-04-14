# Вариант 5

from functools import reduce
a = [1, 2, 3, 4, 5, 6]


def concatenator(st_1, st_2):
    return str(st_1) + str(st_2)


foo = lambda lst: reduce(concatenator, lst)
print(foo(a))


def appender(lst, elem):
    if isinstance(lst, int):
        lst = [lst, elem]
    else: lst.append(elem)
    return lst


foo1 = lambda st: reduce(appender, filter(lambda n: n % 3 == 0, list(map(int, st))))
print(foo1(foo(a)))
