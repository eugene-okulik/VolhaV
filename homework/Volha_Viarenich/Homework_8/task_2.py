# Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число
# На всякий случай, напомню, что превращать результат работы генератора в список - неправильно.

import sys

sys.set_int_max_str_digits(100000)


def fibonacci():
    fibo_1, fibo_2 = 0, 1
    counter = 1
    while True:
        yield fibo_2
        fibo_1, fibo_2 = fibo_2, fibo_1 + fibo_2
        counter += 1


count = 1
for number in fibonacci():
    if count in [5, 200, 1000, 100000]:
        print(number)
    if count == 100000:
        break
    count += 1
