def f1():
    a = 1
    return 0


def f2():
    return f1()


def f3():
    return f2()


f3()
