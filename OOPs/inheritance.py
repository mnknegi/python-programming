
# Inheritance

class Animal:
  def __init__(self, name):
    self.name = name
    self.is_alive = True

  def eat(self):
    print(f"{self.name} is eating.")

  def sleep(self):
    print(f"{self.name} is sleeping.")

class Dog(Animal):
  def speak(self):
    print("WOOF!")

class Cat(Animal):
  def speak(self):
    print("SQUEEK!")

class Mouse(Animal):
  def sleep(self):
    print(f"{self.name} is asleep") # method is overridden

  def speak(self):
    print("WOOF!")

dog = Dog("Scooby")
cat = Cat("Tom")
mouse = Mouse("Jerry")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
cat.speak()

print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()
mouse.speak()