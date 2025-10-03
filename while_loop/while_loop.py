

# name = input("Enter your name: ")

# while name == "":
#   print("You did not enter your name.")
#   name = input("Enter your name: ")

# print(f"Your name is {name}")

food = input("Enter the food you like(press q to quit)")

while not food == "q":
  print(f"You like {food}")
  food = input("Enter another food you like(press q to quit)")

print("bye")