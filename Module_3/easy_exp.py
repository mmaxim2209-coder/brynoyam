class Book:
    book_count = 0
    all_books = [] # список для всех новых книг
    library_name = "Главная библиотека"
    def __init__(self, title="Неизвестно", author="Неизвестно", pages=0):
        self.title = title
        self.author = author
        self.pages = pages
        Book.all_books.append(self) # добавляем книгу в список всех книг
        Book.book_count += 1
        

    def display_info(self):
        print(f"Книга: {self.title}, Автор: {self.author}, Страниц: {self.pages}")
    def is_thick(self):
        return self.pages > 300   
Book1 = Book("1984", "Джордж Оруэлл", 328)
Book2 = Book()
Book3 = Book("Война и мир", "Лев Толстой", 1225)
for book in Book.all_books: # проходим по всем книгам и вызываем метод display_info, шоб автоматически отображать каждую новую книгу
    book.display_info()

print(f"Книга '{Book1.title}' толстая? {Book1.is_thick()}")
print(f"Книга '{Book2.title}' толстая? {Book2.is_thick()}")
for book in Book.all_books: # аналогично с методом is_thick, чтобы отображать результат для каждой новой книги
    print(f"Книга '{book.title}' толстая? {book.is_thick()}")
def change_library_name(new_name):
    Book.library_name = new_name
change_library_name("Центральная библиотека")

print(f"Всего книг: {Book.book_count}")
print(f"Название библиотеки: {Book1.library_name}")
print(f"Название библиотеки: {Book2.library_name}")
#ну реально кайф