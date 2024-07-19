"""A system that tracks books in a library"""

class Book:
    """A Book class with public attributes:
    	title
        author 
        _is_checked_out -> a private attribute to track its availability.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out_book(self, title):
        """Check out a book from library"""
        self._is_checked_out = False

    def return_book(self):
        """Return book to a library"""
        self._is_checked_out = False


class Library():
    """A Library class with
    instance variables:  
    	_books -> a private list to store instances of Book.
    methods:
    	add_book
        check_out_book(title)
        return_book(title)
        list_available_books
    """
    def __init__(self):
        #super().__init__(title, author)
        self._books = []

    def add_book(self, book):
        """Add a book to library"""
        new_book = [book.title, book.author, book._is_checked_out]
        self._books.append(new_book)
        # return self._books

    def check_out_book(self, title):
        """Check out a book from library, if available"""
        for book in self._books:
            if book[0] == title and book[2] is False:
                book[2] = True
                return self.list_available_books()
        print(f"Sorry. We don't have a book by the title {title}")

    def return_book(self, title):
        """Return book to a library"""
        for book in self._books:
            if book[0] == title and book[2] is True:
                book[2] = False
                return self.list_available_books()
        print(f"Sorry. We didn't have a book by the title {title}. Consider adding it as a new book")

    def list_available_books(self):
        """List available books in a library"""
        for book in self._books:
            if book[2] is False:
                  print(book[0] + " by " + book[1])
        #print("Sorry buddy. We are out of books today. Please check in later")

#book1 = Book("Brave New World", "Aldous Huxley")
#print(book1._is_checked_out)
# library = Library()
# library.add_book(Book("Brave New World", "Aldous Huxley"))
# library.add_book(Book("1984", "George Orwell"))
# library.list_available_books()
# library.check_out_book("Brave New World")
# library.return_book("Brave New World")

        