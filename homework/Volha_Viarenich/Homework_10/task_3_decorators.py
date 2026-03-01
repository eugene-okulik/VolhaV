# Напишите программу: Есть функция, которая делает одну из арифметических операций с переданными ей числами
# (числа и операция передаются в аргументы функции). Функция выглядит примерно так:
#
# def calc(first, second, operation):
#     if operation == '+':
#         return first + second
#     elif .....
# Программа спрашивает у пользователя 2 числа (вне функции)
#
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
#
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из первого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение

first_num = int(input("Enter the first number:"))
second_num = int(input("Enter the second number:"))


def calc_decor(func):
    def wrapper(first, second, operation=None):
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        elif first < 0 or second < 0:
            operation = '*'

        return func(first, second, operation)

    return wrapper


@calc_decor
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


print(calc(first_num, second_num))
