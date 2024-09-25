def all_variants(text):
    length = len(text)
    for s in range(1, length + 1):
        for start in range(length - s + 1):
            yield text[start:start + s]

a = all_variants("abc")
for i in a:
    print(i)

