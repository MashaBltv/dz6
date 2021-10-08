try:
    N = int(input('введите количество элементов массива:'))
    a = []
    for i in range(N):
        a.append(int(input('введите элемент массива:')))
    delta = int(input('введите значение delta:'))
    minimum = a[0]
    for i in range(N):
        if a[i] < minimum:
            minimum = a[i]
    counter = 0
    for i in range(len(a)):
        if minimum + delta == a[i]:
            counter += 1
    print('итог:' + str(counter))
except ValueError:
    print('это не число. введите число')