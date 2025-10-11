
# recursion = A func that calls itself from within.

# ITERATIVE
# def walk(steps):
#   for step in range(1, steps + 1):
#     print(f"You take step #{step}")

# RECURSIVE
# def walk(step):
#   if step == 0: # base condition.
#     return
  
#   walk(step - 1)
#   print(f"You take step #{step}")

# walk(100)

# ITERATIVE
def factorial(num):
  result = 1
  if num > 0 :
    for val in range(1, num + 1):
      result *= val
  return result

# RECURSIVE
def recursive_factorial(num):
  if num == 1:
    return 1
  else:
    return num * recursive_factorial(num - 1)

print(recursive_factorial(3))