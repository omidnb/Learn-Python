my_set = {1, 2, 3, 4, 5}  # type: set
print(my_set)

my_set2 = {1, 2, 3, 4, 5, 1, 1, 1, 1, 1, 1}
print(my_set2)

cond1 = my_set is my_set2
print(cond1)  # False

cond2 = 10 in my_set
print(cond2)

print(len(my_set))  # 5
print(len(my_set2))  # 5
