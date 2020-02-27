def factiorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact


print(factiorial(10))


def combination(n, m):
    res = factiorial(n) / (factiorial(n - m) * factiorial(m))
    return int(res)


while True:
    x = int(input('enter : '))
    y = int(input('enter : '))
    print(combination(x, y))
