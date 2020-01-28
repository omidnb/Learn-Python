my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)
print(type(my_list))

length_of_my_list = len(my_list)
print("the length of 'my_list' is", length_of_my_list, "")

print("first element of 'my_list' is", my_list[0])
print("last element of 'my_list' is", my_list[-1])

print("the average of 'my_list' is", sum(my_list) / length_of_my_list)

new_list = my_list[1::2]
print(new_list)  # [2, 4, 6, 8, 10]

print(my_list[8:2:-1])  # [9, 8, 7, 6, 5, 4]
