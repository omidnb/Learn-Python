x = [9, 6, 2, 4, 1]
y = [5, 2, 3, 1, 7]

for i in range(len(x)):
    print(x[i], y[i])

# give us tuple
for obj in zip(x, y):
    print(obj)

# same as range
for a, b in zip(x, y):
    print(a, b)

