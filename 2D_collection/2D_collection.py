
groceries = [
  ["apple", "banana", "pineapple"],
  ["cucumber", "beans", "ladyfinger"],
  ["fish", "chichen", "turkey"]
]

for collection in groceries:
  for food in collection:
    print(food, end=" ")
  print()