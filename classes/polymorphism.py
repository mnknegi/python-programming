# Polymorphism = Greek word that means to "have many forms or faces"
# poly = many
# morphe = faces

# Two ways of achieve polymorphism
# Inheritance = An object could be treated of same type as the parent class.
# Duck Typing = Object must have necessary attributes/methods.

from abc import ABC, abstractmethod

class Shape:
  
  @abstractmethod
  def area(self):
    pass

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return 3.14 * self.radius ** 2

class Square(Shape):
  def __init__(self, side):
    self.side = side

  def area(self):
    return self.side ** 2

class Triangle(Shape):
  def __init__(self, base, height):
    self.base = base
    self.height = height

  def area(self):
    return self.base * self.height * 0.5
  
class Pizza(Circle):
  def __init__(self, topping, radius):
    super().__init__(radius)
    self.topping = topping

circle = Circle(4)
square = Square(5)
triangle = Triangle(base=6, height=7)
pizza = Pizza(topping="pepperoni", radius=15)

shapes = [circle, square, triangle, pizza]

for shape in shapes:
  print(f"{shape.area()} cm^2")