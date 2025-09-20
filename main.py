

print("Hello, World!")

# Strings
first_name = "Mayank Negi"

print(f"Hello, {first_name}")

#  Integers
age = 32
print(f"You are {age} years old.")

# Float
price = 10.99
print(f"The price is: {price}")

# Boolean
isStudent = True

if isStudent:
  print("You are a student.")
else:
  print("You are not a student.")

print(type(first_name))
print(type(age))
print(type(price))
print(type(isStudent))

#  Type Conversion
# Explicit

age = float(age)
print(age)
print(type(age))

isTrue = bool(0)
print(f"True or False: {isTrue}")

# Implicit
x = 2
y = 2.0
x = x / y
print(f"x after implicit type conversion: {x}")