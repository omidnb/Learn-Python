def fun(lst):
    lst.pop(0)
    return lst


list_new = [1, 2, 3, 4]
print(list_new)
list_modified = fun(list_new)
print(list_modified)
print(list_new)
