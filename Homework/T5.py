number = input()
zxc = sum(map(int,str(number)))
if zxc % 3 == 0 and int(number[-1]) % 2 == 0:
    print('делится')
else:
    print('не делится')