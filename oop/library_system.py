"""
Base Class - Book:

Attributes: title (str) and author (str).
Method: __init__(self, title, author) for initializing book attributes.
Derived Classes - EBook and PrintBook:

Both classes inherit from Book.
EBook additional attribute: file_size (int).
PrintBook additional attribute: page_count (int).
Each derived class should have its own __init__ method that 
properly calls the base class __init__ while also initializing its unique attribute.
"""


class Book:
    def __init__(self, title, author):
        self.title = str(title)
        self.author = str(author)


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = int(file_size)


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = int(page_count)


"""
Composition - Library:

Attributes: books (a list to store instances of Book, EBook, and PrintBook).
Methods:
add_book(self, book): Adds a Book, EBook, or PrintBook instance to the library.
list_books(self): Prints details of each book in the library.
"""


class Library:
    def __init__(self):
        self.books = []

    def __str__(self):
        print(f"The library has {len(self.books)}")

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            if hasattr(book, "page_count"):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            elif hasattr(book, "file_size"):
                print(f"Ebook: {book.title} by {book.author}, File Size: {book.file_size}")
            else:
                print(f"Book: {book.title} by {book.author}")
