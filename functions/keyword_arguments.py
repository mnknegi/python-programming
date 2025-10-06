
def hello(greeting, title, first_name, last_name):
  print(f"{greeting} {title}{first_name} {last_name}")

# hello("Hello", "John", "Doe", "Mr.") Hello JohnDoe Mr.
# hello(first_name="John", last_name="Doe", title="Mr.", "Hello") keyword arguments should follow positional arguments.
hello("Hello", first_name="John", last_name="Doe", title="Mr.")