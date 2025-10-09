# Function used in the child class to call methods from the parent class(spuerclass).
# Allow you to extend the functionality of the inherited methods.

class Shape:
  def __init__(self, color, is_filled):
    self.color = color
    self.is_filled = is_filled

  def describe(self):
    print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}.")

class Circle(Shape):
  def __init__(self, color, is_filled, radius):
    super().__init__(color, is_filled)
    self.radius = radius

  def describe(self): # superclass method is overridden here.
    print(f"It is a circle with area of {3.14 * self.radius * self.radius} cm^2")
    super().describe() # Extend the super class method.

class Square(Shape):
  def __init__(self, color, is_filled, width):
    super().__init__(color, is_filled)
    self.width = width
  
  def describe(self): # superclass method is overridden here.
    super().describe() # Extend the super class method.
    print(f"It is a square with area of {self.width * self.width} cm^2")

class Triangle(Shape):
  def __init__(self, color, is_filled, width, height):
    super().__init__(color, is_filled)
    self.width = width
    self.height = height

  def describe(self): # superclass method is overridden here.
    print(f"It is a triangle with area of {self.width * self.height / 2} cm^2")
    super().describe() # Extend the super class method.

circle = Circle(color="red", is_filled=True, radius=5)
print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")
circle.describe()

square = Square(color="green", is_filled=False, width=6)
print(square.color)
print(square.is_filled)
print(f"{square.width}cm")
square.describe()

triangle = Triangle(color="blue", is_filled=True, width=7,height=8)
print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")
triangle.describe()