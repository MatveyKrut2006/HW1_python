text = input('').split('@')
pos = text[0].split()[-1]
per = text[1].split()[0]
print(pos + '@' + per)