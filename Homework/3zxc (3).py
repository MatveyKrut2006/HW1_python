number = input("Введите числа:")
number = [int(x) for x in number.split()]
length = len(number)
if length == 1:
    print("Нет")
elif number == list(range(number[0], number[-1] + 1)):
    print("Да")
else:
    print("Нет")