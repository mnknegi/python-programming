
# reduce(function, collection) = Reduces elements in a collection to a single value.

from functools import reduce

# def add(val1, val2):
#   return val1 + val2

prices = [45.05, 99.0, 34.50, 82.20, 90.0]

# total = reduce(add, prices)
total = reduce(lambda val1, val2: val1 + val2, prices)

print(f"₹{total}")