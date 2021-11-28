"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве
"""
from random import randint

lst = [randint(-5, 5) for i in range(10)]
sor = sorted(lst)
print(sor)
print(f"Максимальный отрицательный элемент = {sor[0]}"
      f"\nПозиция в массиве = {sor.index(sor[0])}")
