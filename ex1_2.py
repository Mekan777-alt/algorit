"""
Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке
и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
"""

while True:
    try:
        users = int(input('\nДобрый день!'
                          '\n1.Подсчитать'
                          '\n0.Выйти'
                          '\n'))

        if users == 1:
            calculate = input("Дерзайте! ")
            try:
                result = eval(calculate)
                print(result)
            except ZeroDivisionError:
                print("На ноль делить нельзя!")
        elif users == 0:
            print("Досвидание!")
            break
    except ValueError:
        print("Неверное значение!"
              "\nПовторите снова")
