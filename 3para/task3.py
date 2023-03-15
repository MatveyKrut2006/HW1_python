summa1 = int(input('введите сумму первого товара:'))
summa2 = int(input('введите сумму второго товара:'))
summa3 = int(input('введите сумму третьего товара:'))
if summa1 <= summa2 and summa2 <= summa3:
    print('Акция!')
    print('К оплате:', (summa1 + summa2 + summa3)//2)
elif summa3 <= summa2 and summa2 <= summa1:
    print('Акция!')
    print('К оплате:', (summa1 + summa2 + summa3)//3)
else:
    print('К оплате:', summa1 + summa2 +summa3)