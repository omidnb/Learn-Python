pattern = "+"
i = 0
limit = 10

while i < limit:
    i = i + 1
    print(pattern * i, end='|')  # end's default is '\n'

sum_1 = 0
y = 0
last_num = 100
while y < last_num:
    y = y + 1
    sum_1 = sum_1 + y
print(id(sum_1), sum_1)
