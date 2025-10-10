
# Static Methods = A method that belong to the class rather than the instance of that class.
#                  usually used for general utility functions.

# Instance methods =  Best for operations on instances of the class.
# Static methods   =  Best for utility functions that do not need access to class data.

class Employee:

  def __init__(self, name, position):
    self.name = name
    self.position = position

  def get_details(self):
    print(f"{self.name} {self.position}")

  # general utility method inside Employee class.
  @staticmethod
  def is_valid_position(position):
    valid_positions = ["Manager", "Cook", "Technology Lead", "Janitor", "Cashier"]
    return position in valid_positions
  
print(Employee.is_valid_position("Technology Lead"))
print(Employee.is_valid_position("Technology Analyst"))

employee1 = Employee("John", "Cook")
employee2 = Employee("Jane", "Cashier")
employee3 = Employee("James", "Manager")

employee1.get_details()
employee2.get_details()
employee3.get_details()

print(employee1.is_valid_position("Manager")) # this will work in a same way as a static method.