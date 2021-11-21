"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""


def sum_n(n):
    sum_1 = 0
    for f in n:
        sum_1 += int(f)
    return sum_1


max_n = 0
max_s = 0
lst_n = [i for i in input("Введите числа: ").split()]
for i in lst_n:
    if sum_n(i) > max_s:
        max_n = i
        max_s = sum_n(i)

print(f'У числа {max_n} была наибольшая сумма цифр - {max_s}')
