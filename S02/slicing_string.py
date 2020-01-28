text = "omid nobahari shabestari"

print(text[::-1])
print(text[::-2])
print(text[::2])

text2 = text[::]

cond1 = text is text2  # True
cond2 = text == text2  # True
print(cond1, cond2)

text_new = text[:3] + 'D' + text[4:]
print(text_new)