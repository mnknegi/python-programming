# List Comprehension - A concise way to create lists in python.
#                      Compact and easier to read than traditional loops.
#                      [expression for value in iterable if condition]

# double = []
# for x in range(1, 11):
#   double.append(x * 2)

# print(double)

double = [x * 2 for x in range(1, 11)]
print(double)

triple = [x * 3 for x in range(1, 11) if x % 2 == 0]
print(triple)

fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)