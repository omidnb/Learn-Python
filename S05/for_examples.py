txt = "You can do anything you set your mind to, man"
txt *= 2
words = txt.split()

for char in words:
    if char[0] in ["a", "b", "c", "d"]:  # char[0] => first character in each word
    # if word.startswith("a"):
        print(char)

# another form

list_a = []
list_b = []

len_a = []
len_b = []

for char in words:
    if char[0] in "abcd":
        list_a.append(char)
        len_a.append(len(char))
    else:
        list_b.append(char)
        len_b.append(len(char))

print(list_a)
print(list_b)
print(len_a)
print(len_b)