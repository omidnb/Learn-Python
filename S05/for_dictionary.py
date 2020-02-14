dct = {
    'key1': "val1",
    'key2': "val2",
    'key3': "val3",
    'key4': "val4",
    'key5': "val5"
}

print(dct.keys())
print(dct.values())

for k in dct:
    print(k, dct[k])

for v in dct.values():  # default is dct.keys
    print(v)

for ke, va in dct.items():
    print(k, v)

dct2 = {
    'k1':
}