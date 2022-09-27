# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random

numbers = int(input('Введите число от 5 до 15: '))
ls = []
for i in range(numbers):
    ls.append(i)
print(ls)
length = len(ls)

j = 0
while j < length:
    a = random.randint(0,length-1)
    b = random.randint(0,length-1)
    num1 = ls[a]
    num2 = ls[b]
    qwerty = num1
    ls[a] = num2
    ls[b]= qwerty
    j += 1
print(ls)