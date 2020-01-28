my_list = [1, 2, 3, 4, 5]
my_list[1] = 1000  # there is no problem
print(my_list)

my_tuple = (1, 2, 3,)  # ',' is not necessary at the end
# my_tuple[1] = 1000  # tuple does not support assignment
print(my_tuple)
my_list = my_list + [9]
print("new list ins", my_list)

my_tuple = my_tuple + (19,)  # ',' is necessary for tuple if it only has 1 element!
print("new tuple is", my_tuple)

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst1[3:8])
print(lst1[3:-2])
print(lst1[3:])
print(lst1[:3])
print(lst1[:5] + lst1[5:])  # complete lst
print(lst1[:5] + [10000] + lst1[5:])
print(lst1)

tup = (1, 2, 3, 4, 5)
tup2 = tup
tup3 = tup[:2] + (99,) + tup2[2:]
print(tup3)

tup4 = tup[:1] + (2,) + tup2[2:]  # (1, 2, 3, 4, 5)
print(tup4)

cond1 = tup is tup4  # False
cond2 = tup == tup4  # True
print(cond1, cond2)
