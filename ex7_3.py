"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
import random
lst = [random.randint(0, 99) for i in range(50)]
print(f'Массив = {lst}')

sort_lst = []
sort_lst.extend(lst)
sort_lst.sort()

print(f"Два наименьших элемента = {sort_lst[0]} и {sort_lst[1]}")
