# Напишите программу, которая добавляет ‘ing’ в конец слов (к каждому слову) в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,
# dignissim vitae libero” и после этого выводит получившийся текст на экран.
# Знаки препинания не должны оказаться внутри слова. Если после слова идет запятая или точка,
# этот знак препинания должен идти после того же слова, но уже преобразованного.

inicial_value = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
                 "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")

# 1

list_value = inicial_value.split(" ")
# new_value = ""
#
# for word in list_value:
#     if word[-1] not in ".,":
#         new_value += (word + "ing" + " ")
#     else:
#         new_value += (word[: -1] + "ing" + word[-1] + " ")
#
# print(new_value)

# 2

result_list = []
for word in list_value:
    if word[-1] not in ".,":
        result_list.append(word + "ing")
    else:
        result_list.append(word[: -1] + "ing" + word[-1])

print(" ".join(result_list))
