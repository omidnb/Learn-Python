vals = [(1, 2), (3, 4), (5, 6)]

# 1
for i in vals:
    print(i)

# 2
for x, y in vals:
    print(x, y)

# 3 (same as #2)
for value in vals:
    x, y = value
    print(x, y)
