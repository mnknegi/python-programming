
age = int(input("Enter your age: "))

if age < 0:
  print("You haven't born yet!")
elif age <= 32:
  print("You are below 33.")
elif age > 32:
  print("You are 33 or plus.")
else:
  print("You are very old.")