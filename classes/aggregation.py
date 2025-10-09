
# Aggregation = Represents a relationship where one object(the whole)
#               contains references to one or more INDEPENDENT objects(the parts).

class Library:
  def __init__(self, name):
    self.name = name
    self.books = []

  def add_book(self, book):
    self.books.append(book)

  def log_books(self):
    for book in self.books:
      print(f"{book.title} by {book.author}")

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

library = Library("New York Public Library")

book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J. R. R. Tolkein")
book3 = Book("The Jungle Book", "Rudyard Kipling")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(f"{library.name}")
library.log_books()