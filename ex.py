num1 = int(input('Введите число 1: '))
num2 = int(input('Введите число 2: '))
num3 = int(input('Введите число 3: '))
num4 = int(input('Введите число 4: '))
num5 = int(input('Введите число 5: '))
list = [num1, num2, num3, num4, num5]
print (list)
max = list[0]

for i in range(len(list)):
    if max < list[i]:
        max = list[i]
print(max)

