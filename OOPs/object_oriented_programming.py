
from car import Car

car1 = Car("BMW", 2025, "red", False)
print(car1) # memory address

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car2 = Car("Audi", 2025, "blue", True)
car3 = Car("Tesla", 2025, "black", True)

car1.drive()
car2.drive()
car3.drive()

car1.stop()
car2.stop()
car3.stop()

car1.description()
car2.description()
car3.description()