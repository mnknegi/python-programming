
# @property = Decorator is used to define a method as a property (it can be accessed like an attribute)
#             Benefit: Add additional logic when read, write or delete attributes.
#             give you getter, setter or deleter method.

class Rectangle:

  def __init__(self, width, height):
    self._width = width
    self._height = height

  # GETTER METHOD  
  @property
  def width(self):
    return f"{self._width:.1f} cm"
  
  @property
  def height(self):
    return f"{self._height:.1f} cm"
  
  # SETTER METHOD
  @width.setter
  def width(self, newValue):
    if newValue > 0:
      self._width = newValue
    else:
      print("Width must be greater than zero")

  @height.setter
  def height(self, newValue):
    if newValue > 0:
      self._height = newValue
    else:
      print("Height must be greater than zero")

  # DELETER METHOD
  @width.deleter
  def width(self):
    del self._width
    print("Width has been deleted.")

  @height.deleter
  def height(self):
    del self._height
    print("Height has been deleted.")

rectangle = Rectangle(3, 4)
print(rectangle.width)
print(rectangle.height)

rectangle.width = 6
rectangle.height = 7
print(rectangle.width)
print(rectangle.height)

del rectangle.width
del rectangle.height
# print(rectangle.width) This will throw an exception as width and height has been deleted.
# print(rectangle.height)