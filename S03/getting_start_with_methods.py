# https://github.com/pymft/mft-vanak/tree/master/S05/string_methods
text = "Hello"

txt1 = text.upper()
txt2 = text.lower()

txt3 = text.upper

print(txt1, txt2, txt3)

lst_of_methods = print(dir(text))

string1 = "omid nobahari shabestari"
print(string1.count("a"))

print(string1.startswith("omid"))  # True

string2 = "Omid Nobahari Shabestari"

print(string1.istitle())  # False
print(string2.istitle())  # True

txt_center = "Omid".center(50)
txt_left_just = "Omid".ljust(50)
txt_right_just = "Omid".rjust(50)

print(txt_center)
print(txt_left_just)
print(txt_right_just)

str_repalce = string2.replace("Nobahari", "NB")
print(str_repalce)

tup = (1, 2, 3, 4, 5, 2, 3, 4)
print(tup.index(2))
print(tup.index(2, 3))  # search after 3th index

words = "aimr mamad matin omid".split()
words *= 5
print(words)

print(words.index("mamad"))  # fist mamad
print(words.index("mamad", 7))  # mamad after 7 (0,1,2,...,7)
print(words.index("mamad", 2, 7))  # mamad between 2 and 7

print(words.count("mamad"))

lst = ["mamad", "omid", "amir", "matin"]
print(lst.append("taylor"))  # none

lst.append("taylor")
print(lst)  # shows taylor

lst.append("taylor")
lst.append("JAFAR")
lst.append("taylor")
print(lst)

lst.remove("taylor")
print(lst)  # removed first 'taylor' from left

# lst.append("a", "b")  ERROR!
lst.extend(["a", "b"])
print(lst)

lst2 = lst.copy()  # COPY doesn't keep main address
lst3 = lst

lst3.append("1000000")
print(lst)  # '1000000' at the end
print(lst2)  # '1000000' didn't append
print(lst3)  # '1000000' at the end

lst.pop(3)  # removed index 3
print(lst)
print(lst2)  # nothing changed because we used COPY to create lst2 and it didn't keep lst address
print(lst3)
