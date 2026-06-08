class Book:
    book_count = 0
    def __init__(self, title="Неизвестно", author="Неизвестно", pages=0):
        self.title = title
        self.author = author
        self.pages = pages
        Book.book_count += 1

    def display_info(self):
        print(f"Книга: {self.title}, Автор: {self.author}, Страниц: {self.pages}")
Book1 = Book("1984", "Джордж Оруэлл", 328)
Book2 = Book()
Book1.display_info()
Book2.display_info()
print(f"Всего книг: {Book.book_count}")


