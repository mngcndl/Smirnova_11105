# Вариант 3

from functools import reduce

leo_seq = lambda n: reduce(lambda m, n: [m[1], m[0] + m[1] + 1], range(n), [1, 1])[0]

for i in range(10):
    print(leo_seq(i))
    