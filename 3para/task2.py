cena = int(input('сумма к оплате:'))
vrem9 = int(input('укажите время:'))

if 8 <= vrem9 <=22:
    if 10 <= vrem9 <= 12:
        print(cena//2)
    if 20 <= vrem9 <= 22:
        print(cena//4)
else:
    print('Магазин закрыт!')