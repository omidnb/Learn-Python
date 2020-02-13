res1 = range(10000)
res2 = list(res1)

print(res1)
print(res2)

print(res1.__sizeof__())
print(res2.__sizeof__())

lst = [1, 2, 3]
x = iter(lst)
print(next(x))
print(next(x))
print(next(x))

for value in range(5, 10, 2):  # from 5 to 10, 2 by 2
    print("*", value)

# another example
start = 0
stop = 100
step = 20

for i in range(start, stop, step):
    print("hello", i)

