pos = 0
neg = 0
n = int
while n != 0:
    n = int(input('Введите число: '))
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1
    elif n == 0:
        break
print ('кол-во положительных чисел', pos)
print ('кол-во отрицательных чисел', neg)