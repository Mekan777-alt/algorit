"""Определить, какое число в массиве встречается чаще всего"""

import random

s = [random.randint(0, 20) for i in range(20)]
print(f"Первый список = {s}")
print(max(a for a in s if s.count(a) == max(map(s.count, s))))
