f = lambda x: x ** 3
print(f(2))

is_even = lambda n: n % 2 == 0
print(is_even(16))

word_counter = lambda text: len(text.split())
n = word_counter("all i have in this world is my balls and my word and i don't break them for no one")
print(n)

# abcd --> abcddcba
mirror = lambda text: text + text[::-1]
print(mirror("abcd"))