"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
"""
import random

mass = [random.randint(0, 100) for i in range(10)]
print(f"Список до изменение {mass}")
min_mass = min(mass)
max_mass = max(mass)
for i in range(len(mass)):
    if mass[i] == max_mass:
        mass[i] = min_mass
    elif mass[i] == min_mass:
        mass[i] = max_mass

print(f"Список после изменение {mass}")
