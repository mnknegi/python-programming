
# .sort() or sorted()
# sort lists[], tuples(), dictionaries{"":""}, objects

# ----------- List -----------

fruits = ["banana", "orange", "apple", "coconut"]
numbers = [3, 1, 5, 2, 4]

fruits.sort()
numbers.sort(reverse=True) # sort in reverse order.

print(fruits)
print(numbers)

# ----------- Tuple -----------

directions = ("east", "west", "north", "south")

# sorted_directions = sorted(directions) # This will return a list
# sorted_directions = tuple(sorted_directions) # converted into a tuple
sorted_directions = tuple(sorted(directions, reverse=True)) # sorted in reverse order

print(sorted_directions)

# ----------- Dictionary -----------

directions = {"east": 1, 
              "west": 2, 
              "north": 3, 
              "south": 4}

# sorted by key
# directions = dict(sorted(directions.items()))
# directions = dict(sorted(directions.items(), key=lambda item: item[0], reverse=True))

# directions = dict(sorted(directions.items(), key=lambda item: item[1]))
directions = dict(sorted(directions.items(), key=lambda item: item[1], reverse=True))
print(directions)

# ----------- Dictionary -----------

class Fruit:
  def __init__(self, name, calories):
    self.name = name
    self.calories = calories

  def __repr__(self):
    return f"{self.name}: {self.calories}"
  
fruits = [Fruit("banana", 105), 
          Fruit("apple", 72), 
          Fruit("orance", 73),
          Fruit("coconut", 354)]

fruits = sorted(fruits, key=lambda fruit: fruit.name)
fruits = sorted(fruits, key=lambda fruit: fruit.calories)
fruits = sorted(fruits, key=lambda fruit: fruit.name, reverse=True)
fruits = sorted(fruits, key=lambda fruit: fruit.calories, reverse=True)

print(fruits)