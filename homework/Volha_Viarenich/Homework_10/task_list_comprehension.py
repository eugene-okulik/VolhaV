# Дан такой кусок прайс листа:
# (Копируйте эту переменную (константу) в код прямо как есть)
# При помощи list comprehension и/или dict comprehension превратите этот текст в словарь такого вида:

# {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}

PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

transfer_to_list = PRICE_LIST.split('\n')

new_list = [tuple(x.split(' ')) for x in transfer_to_list]
new_dict = {key: int(value[:-1]) for key, value in new_list}
# new_dict = dict(new_list)

print(new_dict)
