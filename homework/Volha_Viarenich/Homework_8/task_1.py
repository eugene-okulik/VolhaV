# Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool.
# Спросите у пользователя salary. А bonus пусть назначается рандомом.
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.
# Примеры результатов:
# 10000, True - '$10255'
# 25000, False - '$25000'
# 600, True - '$3785'

import random

user_salary = int(input("Input your salary: "))


def total_salary(salary):
    bonus = [True, False]
    if random.choice(bonus):
        return salary + random.randint(100, 10000)
    else:
        return salary


print(total_salary(user_salary))
