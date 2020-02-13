text = """"His palms are sweaty, knees weak, arms are heavy
There's vomit on his sweater already, mom's spaghetti
He's nervous, but on the surface he looks calm and ready
To drop bombs, but he keeps on forgettin'
"""
# print(text)
words = text.split()
unique_words = set(words)
print(unique_words)
for w in unique_words:
    print(words.count(w), w)