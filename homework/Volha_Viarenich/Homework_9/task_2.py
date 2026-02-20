# С помощью функции map или filter создайте из этого списка новый список с жаркими днями.
# Будем считать жарким всё, что выше 28.
# Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.


temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23,
                25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

hot_temperature = list(filter(lambda x: x > 28, temperatures))

print(max(hot_temperature))
print(min(hot_temperature))
print(sum(hot_temperature) // len(hot_temperature))
