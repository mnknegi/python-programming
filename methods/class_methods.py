# class methods = Allow operations related to class itself.
#                 Take (cls) as a first parameter, which represents a class itself.

class Student:

  student_count = 0

  def __init__(self, name, age):
    self.name = name
    self.age = age
    Student.student_count += 1

  # INSTANCE METHOD 
  def get_info(self):
    print(f"{self.name} {self.age}")

  # CLASS METHOD
  @classmethod
  def get_count(cls):
    return f"Total # of students {cls.student_count}"
  
student1 = Student("John", 26)
student2 = Student("Jane", 24)
student3 = Student("James", 16)

student1.get_info()
student2.get_info()
student3.get_info()

print(Student.get_count())