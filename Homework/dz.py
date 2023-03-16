zxc = "ААААBBBCCF"
result = ""

for i in set(zxc):
    number = zxc.count(zxc[0])
    result += str(number)
    result += zxc[0]
    zxc = [j for j in zxc if j != zxc[0]]

print(result)