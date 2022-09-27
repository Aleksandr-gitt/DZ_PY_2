# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

# num = float(input('Введите число: '))
# qwe = len(str(num))
# newnum = int(num * (10 ** (qwe-1)))
# sum = 0
# for i in str(newnum):
#     sum = sum + int(i)
# print(sum)

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

# n = int(input('Введите число: '))
# num = 1
# ls = []
# for i in range(1, n+1):
#     num = num * i
#     ls.append(num)
# print(ls)

# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

#     Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

# n = int(input('Введите число: '))
# sum = 0
# for i in range(1, n+1):
#     num = int((1+1/n)**n)
#     sum = sum + num
#     # print(num)
# print(sum)

# * 4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).

# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

# num1 = int(input('Введите первый множитель: '))
# num2 = int(input('Введите второй множитель: '))
# N = int(input('Введите число: '))
# ls =[]
# for i in range (-N, N+1):
#     ls.append(i)
# # print(ls)
# res = ls[num1-1] * ls[num2-1]
# print(res)

# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random

numbers = int(input('Введите число от 5 до 10: '))
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

