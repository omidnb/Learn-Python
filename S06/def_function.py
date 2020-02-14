f = lambda x: x ** 3


def y(x):
    res = x ** 2
    return res


def fact(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s


print(f(2))
print(y(2))
print(fact(10))