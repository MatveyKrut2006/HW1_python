number = 5
zxc = input('введите (game), если хотите перейти в раздел развлечений, (off - завершить)\n').lower()
if zxc == 'game':
    print('запущена игра угадай число')
    while True:
        tru = int(input('введите число:'))
        if tru == number:
            print('Вы выиграли билеты на концерт!')
            break
        elif tru is not number:
            print('попробуйте еще раз:')
if zxc == 'off':
    print('пока, пока!')