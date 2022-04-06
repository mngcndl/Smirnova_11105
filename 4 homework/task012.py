from functools import partial


def calculate(ar1: int, opr1: str, ar2: int, opr2: str, ar3: int, opr3: str, ar4: int, opr4: str, ar5: int) -> float:
    opers = [opr1, opr2, opr3, opr4]
    args = [ar1, ar2, ar3, ar4, ar5]
    for i in range(4):
        if opers[i] == '+':
            res = args[0] + args[1]
            args.pop(0)
            args[0] = res
        elif opers[i] == '*':
            res = args[0] * args[1]
            args.pop(0)
            args[0] = res
        elif opers[i] == '/':
            res = args[0] / args[1]
            args.pop(0)
            args[0] = res
        else:
            res = args[0] - args[1]
            args.pop(0)
            args[0] = res
    return args.pop()


print(calculate(1, '+', 1, '*', 2, "-", 3, "/", 10))


def curried_calculate(ar1: int):
    def oper1(opr1: str):
        def arg2(ar2: int):
            def oper2(opr2: str):
                def arg3(ar3: int):
                    def oper3(opr3: str):
                        def arg4(ar4: int):
                            def oper4(opr4: str):
                                def arg5(ar5: int):
                                    print(str(ar1) + opr1 + str(ar2) + opr2 + str(ar3) + opr3 + str(ar4) + opr4 + str(
                                        ar5))
                                    return eval(
                                        str(ar1) + opr1 + str(ar2) + opr2 + str(ar3) + opr3 + str(ar4) + opr4 + str(
                                            ar5))

                                return arg5

                            return oper4

                        return arg4

                    return oper3

                return arg3

            return oper2

        return arg2

    return oper1


print(curried_calculate(1)('+')(1)('*')(2)('-')(3)('/')(10))
# eval считает ответ по приоритетности операций, а мой метод - нет, поэтому ответы отличаются


listed_opers = ['+', '*', '-', '/']
listed_args = [1, 1, 2, 3, 10]


def calculate_for_partial(args, opers) -> float:
    for i in range(4):
        if opers[i] == '+':
            res = args[0] + args[1]
            args.pop(0)
            args[0] = res
        elif opers[i] == '*':
            res = args[0] * args[1]
            args.pop(0)
            args[0] = res
        elif opers[i] == '/':
            res = args[0] / args[1]
            args.pop(0)
            args[0] = res
        else:
            res = args[0] - args[1]
            args.pop(0)
            args[0] = res
    return args.pop()


new_calc = partial(calculate_for_partial, args=listed_args)
print(new_calc(opers=listed_opers))
