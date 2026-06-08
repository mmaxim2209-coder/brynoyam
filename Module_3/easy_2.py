class Book:
    book_count = 0
    library_name = "Главная библиотека"
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

def change_library_name(new_name):
    Book.library_name = new_name
change_library_name("Центральная библиотека")

print(f"Всего книг: {Book.book_count}")
print(f"Название библиотеки: {Book1.library_name}")
print(f"Название библиотеки: {Book2.library_name}")