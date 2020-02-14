text = """"His palms are sweaty, knees weak, arms are heavy
There's vomit on his sweater already, mom's spaghetti
"""

words = text.split()

# First Form
for w in range(len(words)):
    print(w, words[w])

# give us tuple
for w in enumerate(words):
    print(w)

# another form (same as First Form)
for i, w in enumerate(words):
    print(i, w)

