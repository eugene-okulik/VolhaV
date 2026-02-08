my_dict = {'tuple': ("a", "b", "c", "d", "e", "f", "j", "h"),
           'list': [1, 2, 3, 4, 1, 2, 3, 4],
           'dict': {'Python': 'Гвидо ван Россум',
                    'C#': 'Андерс Хейлсберг',
                    'Java': 'Джеймс Гослинг',
                    'C++': 'Бьёрн Страуструп',
                    'JavaScript': 'Брендан Эйх'
                    },
           'set': {"Python", "is", "the", "best", "language", 'ever'}
           }
# ‘tuple’: выведите на экран последний элемент
print(my_dict['tuple'][-1])

# ‘list’: добавьте в конец списка еще один элемент
my_dict['list'].append(5)
# ‘list’: удалите второй элемент списка
my_dict['list'].pop(1)

# ‘dict’: добавьте элемент с ключом ('i am a tuple',) и любым значением
my_dict['dict']['i am a tuple'] = True

# ‘dict’:удалите какой-нибудь элемент
del my_dict['dict']['JavaScript']

# ‘set’: добавьте новый элемент в множество
my_dict['set'].add('!')
# ‘set’: удалите элемент из множества
my_dict['set'].remove('is')

print(my_dict)
