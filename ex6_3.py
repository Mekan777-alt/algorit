"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint

lst = [randint(0, 50) for i in range(15)]
print(f"Начальный список {lst}")

max_id = 0
min_id = 0
for i in range(1, len(lst)):
    if lst[i] < lst[min_id]:
        min_id = i
    elif lst[i] > lst[max_id]:
        max_id = i
if min_id > max_id:
    min_id, max_id = max_id, min_id
summ = 0
for i in range(min_id+1, max_id):
    summ += lst[i]
print(f"Сумма элементов между минимальным и максимальным значением = {summ}")
