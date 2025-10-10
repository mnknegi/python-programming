
# Magic Methods = Dunder methods(double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of the Python's build-in operations.
#                 They allow developers to define or customized the behavior of objects.

class Book:

  def __init__(self, title, author, page_num):
    self.title = title
    self.author = author
    self.page_num = page_num

  def __str__(self):
    return f"'{self.title}' by {self.author}"
  
  def __eq__(self, other):
    return self.title == other.title and self.author == other.author
  
  def __lt__(self, other):
    return self.page_num < other.page_num
  
  def __add__(self, other):
    return self.page_num + other.page_num
  
  def __contains__(self, keyword):
    return keyword in self.title or keyword in self.author
  
  def __getitem__(self, key):
    if key == "title":
      return self.title
    elif key == "author":
      return self.author
    elif key == "page_num":
      return self.page_num
    else:
      return f"key {key} not found!"
  
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's stone", "J.K. Rowling", 223)
book3 = Book("The Jungle Book", "Rudyard Kipling", 277)
book4 = Book("The Jungle Book", "Rudyard Kipling", 167)

# after __str__ this will show customized string instead of raw memory address.
# This is similar to string(describing:) in Swift
print(book1)
print(book2)
print(book3)

# This will be false until __eq__ is implemented.
# This is similar to conforming to equality protocol in Swift.
print(book3 == book4)

# This will throw an error: '<' not supported between instances of 'Book' and 'Book' until __lt__ is implemented.
# This is similar to conforming to comparable protocol in Swift.
print(book3 < book4)
print(book1 > book3)

# This will throw an error: TypeError: unsupported operand type(s) for +: 'Book' and 'Book' until __add__ is implemented.
print(book1 + book2)

# This will throw an error: TypeError: argument of type 'Book' is not iterable until __contains__ is implemented.
print("Jungle" in book3)

# This will throw an error: TypeError: 'Book' object is not subscriptable until __getitem__ is implemented.
print(book3['title'])
print(book3['author'])
print(book3['page_num'])
print(book3['table_of_content'])