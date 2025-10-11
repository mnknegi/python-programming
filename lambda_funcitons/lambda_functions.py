
# used with 'sort()', 'map()', 'filter()', 'reduce()'
# lambda parameter: expression

double = lambda x: x * 2
add = lambda x, y: x + y
max_value = lambda val1, val2: val1 if val1 > val2 else val2

full_name = lambda first_name, last_name: first_name + " " + last_name
valid_age = lambda age: True if age >= 18 else False

print(double(4))
print(add(3, 4))
print(max_value(4, 6))
print(max_value(8, 6))

print(full_name("John", "Doe"))
print(valid_age(17))