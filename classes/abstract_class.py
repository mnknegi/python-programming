
# Abstract class

# A class that can't be instantiated on its own. Meant to be subclassed.
# These classes contains abstract methods, which are declared but have no implementation.
# This works like protocols in Swift and Interface in Android.

from abc import ABC, abstractmethod

class Vehicle(ABC):
  
  @abstractmethod
  def go(self):
    pass

  @abstractmethod
  def stop(self):
    pass

# vehicle = Vehicle() 
# TypeError: Can't instantiate abstract class Vehicle without an implementation for abstract methods 'go', 'stop'

class Car(Vehicle):
  def go(self):
    print("You drive the car.")

  def stop(self):
    print("You stop the car.")

car = Car()
# Without implementing go and stop method in Car class we will get below error.
# TypeError: Can't instantiate abstract class Car without an implementation for abstract methods 'go', 'stop'
car.go()
car.stop()

class Motorcycle(Vehicle):
  def go(self):
    print("You ride the motorcycle.")

  def stop(self):
    print("You stop the motorcycle.")

motorcycle = Motorcycle()
motorcycle.go()
motorcycle.stop()

class Boat(Vehicle):
  def go(self):
    print("You sail the boat.")

  def stop(self):
    print("You anchor the boat.")

boat = Boat()
boat.go()
boat.stop()