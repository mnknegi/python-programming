
class Student:

  class_year = 2025
  number_of_students = 0

  def __init__(self, name, age):
    self.name = name
    self.age = age
    Student.number_of_students += 1

student1 = Student("John", 32)
student2 = Student("Jane", 28)
student3 = Student("James", 14)

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)

# print(student1.class_year)
# print(student2.class_year)

print(Student.class_year)
print(Student.number_of_students)