# Создайте класс book с атрибутами:
#
# материал страниц
# наличие текста
# название книги
# автор
# кол-во страниц
# ISBN
# флаг зарезервирована ли книга или нет (True/False).
# Какие-то из атрибутов будут общими для всех книг (материал, наличие текста), какие-то индивидуальными.
# Создайте несколько (штук 5) экземпляров разных книг.
# После создания пометьте одну книгу как зарезервированную.
# Распечатайте детали о каждой книге в таком виде:
# Если книга зарезервирована:
#
# Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага, зарезервирована
# если не зарезервирована:
#
# Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага


class Book:
    pages_material = 'paper'
    text = True

    def __init__(self, title, author, ibsn, quantity_of_pages, is_reserved):
        self.title = title
        self.author = author
        self.ibsn = ibsn
        self.quantity_of_pages = quantity_of_pages
        self.is_reserved = is_reserved


class HorrorBook(Book):
    def __init__(self, title, author, ibsn, quantity_of_pages, is_reserved):
        super().__init__(title, author, ibsn, quantity_of_pages, is_reserved)

    def book_description(self):
        reserved = ', зарезервирована' if self.is_reserved else ''
        print(
            f'Название: {self.title}, Автор: {self.author}, страниц: {self.quantity_of_pages}, '
            f'материал: {self.pages_material}{reserved}'
        )


if __name__ == "__main__":
    dark_tower = HorrorBook("Dark Tower", "Stephen King", '5-17-033693-4', 816, True)
    chapaev_i_pustota = HorrorBook("Чапаев и Пустота", "В. Пелевин", "1-17-033693-2", 384, False)
    shining = HorrorBook("The Shining", "Stephen King", '7-17-033693-8', 640, False)
    interview = HorrorBook("Interview with the vampire", "Anne Race", None, 583, False)
    twin_peaks = HorrorBook("Twin Peaks", "Mark Frost", '9-17-033693-8', 777, False)

    dark_tower.book_description()
    chapaev_i_pustota.book_description()
    shining.book_description()
    interview.book_description()
    twin_peaks.book_description()
