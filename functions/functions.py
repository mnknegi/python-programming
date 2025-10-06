
def greeting(name, age):
  print(f"Hello, {name}")
  print(f"You are {age} years old.")
  print("bye")
  print()

greeting("Mayank", 32)
greeting("Ved", 4)
greeting("Vaasu", 4)

# return statement
def add(val1, val2):
  sum = val1 + val2
  return sum

print(add(1, 2))

def create_name(first_name, last_name):
  first_name = first_name.capitalize()
  last_name = last_name.capitalize()
  return first_name + " " + last_name

full_name = create_name("mayank", "negi")

print(full_name)
