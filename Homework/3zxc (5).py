spisok = [0, 0, 0, 0, 0]
count = int(input('введите оценки:'))
while count != -1:
    spisok[count -1] += 1
    count = int(input('введите оценки:'))
total = 0
for i in range(2, 5):
    total =+spisok[i]
print('spis: ', end='')
for i in range(5):
    for g in range(spisok[i]):
        print(i + 1, end=' ')
print("\nNumber of spis: " + ''.join(str(spisok) +
      "\nAcademic performance: " + str(total / sum(spisok) * 100)))