# Decorators = A function that extends the behavior of another function.
#              w/0 modifying the base function
#              pass the base function as an argument of the function

#              @add_sprinkles
#              get_ice_cream("vanilla")

def add_sprinkles(func):
  def wrapper(*args, **kwargs):
    print("add some sprinkles 🎉")
    func(*args, **kwargs)
  return wrapper

def add_fudge(func):
  def wrapper(*args, **kwargs):
    print("add some fudge 🍫")
    func(*args, **kwargs)
  return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
  print(f"Here is your {flavor} ice cream 🍨")

get_ice_cream("vanilla")