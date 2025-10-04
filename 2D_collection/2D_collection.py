
# groceries = [
#   ["apple", "banana", "pineapple"],
#   ["cucumber", "beans", "ladyfinger"],
#   ["fish", "chichen", "turkey"]
# ]

# for collection in groceries:
#   for food in collection:
#     print(food, end=" ")
#   print()

num_pad = ((1, 2, 3), 
           (4, 5, 6), 
           (7, 8, 9), 
           ("*", 0, "#"))

print()
for row in num_pad:
  for num in row:
    print(num, end="    ")
  print()

print()