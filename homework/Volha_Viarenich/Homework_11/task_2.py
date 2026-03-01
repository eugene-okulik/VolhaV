# Создайте дочерний класс для первого. Это будет класс для школьных учебников. В нем будут дополнительные атрибуты:
#
# предмет (типа математика, история, география),
# класс (школьный класс, для которого этот учебник)(осторожно с названием переменной.
# class - зарезервированное слово),
# наличие заданий (bool)
# Создайте несколько экземпляров учебников.
# После создания пометьте один учебник как зарезервированный.
# Распечатайте детали о каждом учебнике в таком виде: Если учебник зарезервирован:
#
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9, зарезервирована
# если не зарезервирован:
#
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9

from task_1 import Book


class SchoolBook(Book):
    def __init__(self, title, author, ibsn, quantity_of_pages, is_reserved, subject, school_class_value, is_task):
        super().__init__(title, author, ibsn, quantity_of_pages, is_reserved)
        self.subject = subject
        self.school_class_value = school_class_value
        self.is_task = is_task

    def school_description(self):
        print(
            f'Название: {self.subject}, Автор: {self.author}, страниц: {self.quantity_of_pages}, '
            f'материал: {self.pages_material}'
            f'{', зарезервирована' if self.is_reserved else ''}'
        )


math = SchoolBook("Алгебра", "Иванов", None, 250, True, "Математика", 5, True)
georaphy = SchoolBook("География", "Петров", '8-17-033693-4', 199, False, "География РБ", 9, True)
biology = SchoolBook("Анатомия", "Сидоров", '8-11-033693-4', 248, False, "Биология", 6, False)
physics = SchoolBook("Астрономия", "Хокинг", None, 333, False, "Физика", 11, False)
foreign_language = SchoolBook("English", "Smith", '2-33-033693-9', 500, False, "Иностранный язык", 8, True)

math.school_description()
georaphy.school_description()
biology.school_description()
physics.school_description()
foreign_language.school_description()
