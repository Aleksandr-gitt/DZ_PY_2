# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

num = float(input('Введите число: '))
qwe = len(str(num))
newnum = int(num * (10 ** (qwe-1)))
sum = 0
for i in str(newnum):
    sum = sum + int(i)
print(sum)


