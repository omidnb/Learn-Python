i = 1
y = 10
while i < y:
    i += 1
    print("omid")
    # if i > 5:
    #     break
else:
    print("this 'else' is for 'while'")  # instead of if break


# # fibonacci
# limit = 20
# list_fib = [1, 1]
#
# while len(list_fib) < limit:
#     new_element = list_fib[-1] + list_fib[-2]
#     list_fib.append(new_element)
# print(list_fib)

fib = [1, 1]
for x in range(10):
    res = fib[-1] + fib[-2]
    fib.append(res)
    print(res)