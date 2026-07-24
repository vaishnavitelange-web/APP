class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed = ""


class Library:
    def __init__(self):
        self.book = None
        self.patron = None

    def add_book(self, title, author):
        self.book = Book(title, author)
        print("Book Added:", title)

    def register_patron(self, name):
        self.patron = Patron(name)
        print("Patron Registered:", name)

    def borrow_book(self):
        if self.book.available:
            self.book.available = False
            self.patron.borrowed = self.book.title
            print(self.patron.name, "borrowed", self.book.title)
        else:
            print("Book is not available.")

    def return_book(self):
        if self.patron.borrowed == self.book.title:
            self.book.available = True
            self.patron.borrowed = ""
            print("Book Returned Successfully.")
        else:
            print("No book to return.")

    def show_details(self):
        print("\nLibrary Details")
        print("Book:", self.book.title)
        print("Author:", self.book.author)
        print("Available:", self.book.available)
        print("Patron:", self.patron.name)
        print("Borrowed Book:", self.patron.borrowed)


# Main Program
library = Library()

library.add_book("Python Programming", "Guido van Rossum")
library.register_patron("Vaishnavi")

library.borrow_book()
library.show_details()

library.return_book()
library.show_details()