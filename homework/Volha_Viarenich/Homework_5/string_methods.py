# 1. С помощью распаковки создайте из этого списка переменные, содержащие соответствующие данные:
# name, last_name, city, phone, country

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

# 2. С помощью срезов и метода index получите из каждой строки с результатом число, прибавьте к полученному числу 10, результат сложения распечатайте.
result_1 = "результат операции:42"
result_2 = "результат операции: 514"
result_3 = "результат работы программы: 9"

if result_1[result_1.find(":") + 1] != ' ':
    index_number_1 = result_1.find(":") + 1
else:
    index_number_1 = result_1.find(":") + 2
print(int(result_1[index_number_1::]) + 10)

if result_2[result_2.find(":") + 1] != ' ':
    index_number_2 = result_2.find(":") + 1
else:
    index_number_2 = result_2.find(":") + 2
print(int(result_2[index_number_2::]) + 10)

if result_3[result_3.find(":") + 1] != ' ':
    index_number_3 = result_3.find(":") + 1
else:
    index_number_3 = result_3.find(":") + 2
print(int(result_3[index_number_3::]) + 10)

# 3. Распечатайте текст, который будет использовать данные из этих списков. Текст в итоге должен выглядеть так: Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geography
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

student_1, student_2, student_3 = students
subject_1, subject_2, subject_3 = subjects

print(f"Students {student_1}, {student_2}, {student_3} study these subjects: {subject_1}, {subject_2}, {subject_3}")
