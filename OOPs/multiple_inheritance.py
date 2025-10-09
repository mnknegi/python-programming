
# multiple inheritance & multi-level inheritance in python

class Animal:

  def __init__(self, name):
    self.name = name

  def eat(self):
    print(f"{self.name} animal is eating")

  def sleep(self):
    print(f"{self.name} animal is sleeping")

class Pray(Animal):
  def flee(self):
    print(f"{self.name} animal is fleeing")

class Predator(Animal):
  def hunt(self):
    print(f"{self.name} animal is hunting")

class Rabbit(Pray):
  pass

class Hawk(Predator):
  pass

class Fish(Pray, Predator):
  pass

rabbit = Rabbit("Bunny")
hawk = Hawk("Falcon")
fish = Fish("Nemo")

rabbit.flee()

hawk.hunt()

fish.flee()
fish.hunt()

rabbit.eat()
rabbit.sleep()

hawk.eat()
hawk.sleep()

fish.eat()
fish.sleep()