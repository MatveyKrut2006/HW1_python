nastolka = input('введите настольную игру:\n').lower()
spit = []
while nastolka != '0':
    if nastolka not in spit:
        spit.append(nastolka)
    else:
        print('эта игра уже записана')
    nastolka = input()