"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
"""
import collections

while True:
    try:
        n_comp = int(input('Введите количество компаний: '))
    except ValueError:
        print('Вы ввели недопустимое значение')
        continue
    break

companies = collections.defaultdict()
len_c = collections.deque()
unproven_c = collections.deque()
all_profit = 0
QUARTER = 4

for i in range(n_comp):
    name = input(f'\nВведите название {i+1}й компании: ')
    profit = 0
    q = 1
    while q <= QUARTER:
        try:
            profit += float(input(f'Введите прибыль за {q}й квартал: '))
        except ValueError:
            print('Вы ввели недопустимое значение')
            continue
        q += 1
    companies[name] = profit
    all_profit += profit

mid_profit = all_profit / n_comp
for i, item in companies.items():
    if item >= mid_profit:
        len_c.append(i)
    else:
        unproven_c.append(i)
print(f'Средняя прибыль для всех компаний: {mid_profit}')
print(f'Прибыль выше среднего у {len(len_c)} компаний:')
for name in len_c:
    print(name)
print(f'Прибыль ниже среднего у {len(unproven_c)} компаний:')
for name in unproven_c:
    print(name)
