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

# more examples
f1 = lambda x: x ** 2  # print((lambda x: x ** 2)(5))
print(f1(5))


def f2(x):
    res = x ** 2
    return res


print(f2(5))


# point distance
def distance(p):
    dist = p[0] ** 2 + p[1] ** 2
    res = dist ** 0.5
    return res


point = (10, 20)
res_1 = distance(point)
print(res_1)

# anothr form for point distance
val = 50  # Global


def distance2(x, y):
    dist = x ** 2 + y ** 2
    res = dist ** 0.5 + val
    return res


res_2 = distance2(10, 20)
print(res_2)
