from collections.abc import Iterator, Iterable

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'"{self.title}", автор {self.author}'

class BookIterator(Iterator):
    def __init__(self, book_collection):
        self._collection = book_collection
        self._index = 0

    def __next__(self):
        try:
            book = self._collection[self._index]
        except IndexError:
            raise StopIteration()
        self._index += 1
        return book

class BookCollection(Iterable):
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def __iter__(self):
        return BookIterator(self._books)

# Пример использования
book_collection = BookCollection()
book_collection.add_book(Book("Капитанская дочка", "А. С. Пушкин"))
book_collection.add_book(Book("Война и мир", "Л. Н. Толстой"))
book_collection.add_book(Book("Преступление и наказание", "Ф. М. Достоевский"))
book_collection.add_book(Book("Евгений Онегин", "А. С. Пушкин"))
book_collection.add_book(Book("Обломов", "И. А. Гончаров"))

for book in book_collection:
    print(book)