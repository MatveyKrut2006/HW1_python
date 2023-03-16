log = input('введите логин:\n').lower()
password = '=?*^$№@_'
choto = ''
for i in log:
    for x in password:
        if i == x:
            choto += x
print(choto)