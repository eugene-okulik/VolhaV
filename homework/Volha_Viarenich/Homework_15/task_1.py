import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)
cursor = db.cursor(dictionary=True)


# 1. Создайте студента (student)
cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES ('Volha', 'Sidorova', NULL)")
student_id = cursor.lastrowid

# 2. books Создайте несколько книг (books) и укажите, что ваш созданный студент взял их.
insert_books_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    insert_books_query, [
        ('Dark Tower', student_id),
        ('Twin Peaks', student_id),
        ('Python AQA for Beginners', student_id)
    ]
)

# 3. Создайте группу (group) и определите своего студента туда.
cursor.execute(
    "INSERT INTO `groups`(title, start_date, end_date) VALUES ('Python AQA Engineers', '19-01-2026', '19-07-2026')")
group_id = cursor.lastrowid
cursor.execute(f"UPDATE students SET group_id = {group_id} WHERE id = {student_id}")

# 4.Создайте несколько учебных предметов (subjects)
cursor.execute("INSERT INTO subjects (title) VALUES ('Biology of frogs')")
subject_1_id = cursor.lastrowid
cursor.execute("INSERT INTO subjects (title) VALUES ('Astronomy of sun system')")
subject_2_id = cursor.lastrowid
subject3 = cursor.execute("INSERT INTO subjects (title) VALUES ('Blueberry eating')")
subject_3_id = cursor.lastrowid

# Создайте по два занятия для каждого предмета (lessons)
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('Frogs intro', {subject_1_id})")
lesson_1_1_id = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('Frogs final', {subject_1_id})")
lesson_1_2_id = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('Sun system intro', {subject_2_id})")
lesson_2_1_id = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('Sun system final', {subject_2_id})")
lesson_2_2_id = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('Blueberry intro', {subject_3_id})")
lesson_3_1_id = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('Blueberry final', {subject_3_id})")
lesson_3_2_id = cursor.lastrowid

# Поставьте своему студенту оценки (marks) для всех созданных вами занятий
# Все действия нужно выполнить именно в том порядке, который указан здесь в задании.
insert_marks_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_marks_query, [
        (9, lesson_1_1_id, student_id),
        (8, lesson_1_2_id, student_id),
        (8, lesson_2_1_id, student_id),
        (10, lesson_2_2_id, student_id),
        (9, lesson_3_1_id, student_id),
        (9, lesson_3_2_id, student_id)
    ]
)

# Получите информацию из базы данных:

# Все оценки студента
cursor.execute(f"SELECT * FROM marks WHERE student_id = {student_id}")
marks_data = cursor.fetchall()
print(marks_data)

# Все книги, которые находятся у студента
cursor.execute(f"SELECT * FROM books WHERE taken_by_student_id = {student_id}")
taken_books_data = cursor.fetchall()
print(taken_books_data)

# Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
# (всё одним запросом с использованием Join)

student_data = f'''
SELECT
name,
second_name,
`groups`.title AS group_title,
books.title AS book_taken_by_student,
subjects.title AS subject,
lessons.title AS lesson,
marks.value AS mark_value
FROM students
join `groups`
ON students.group_id = groups.id
join books
ON students.id = books.taken_by_student_id
join marks
ON students.id = marks.student_id
join lessons
ON marks.lesson_id = lessons.id
join subjects
ON lessons.subject_id = subjects.id
WHERE students.id = {student_id}
'''

cursor.execute(student_data)
student_data_result = cursor.fetchall()
print(student_data_result)

db.commit()
db.close()
