newspaper = range(1, 76)
magazine = range(77, 104)
both = range(21, 34)
a = (magazine - both)
b = len((newspaper | a))
print(list(a))