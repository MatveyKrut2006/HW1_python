marki = [0, 0, 0, 0, 0]
mark = int(input("Введите значение: "))

while mark != -1:
    marki[mark - 1] += 1
    mark = int(input("введите значение: "))

percent = marki[-1] / sum(marki) * 100
print("Percent of 5's is %s" % int(percent) + '%')