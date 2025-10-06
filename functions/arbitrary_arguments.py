
# *args -> pass as a tuple
# **kwargs -> pass as a dictionary
# *unpacking operator

# *args
def add(*nums):
  total = 0
  for num in nums:
    total += num
  return total

print(add(1,2,3))

# *kwargs
def address(**kwargs):
  # for value in kwargs.values():
  #   print(value)
  for key, value in kwargs.items():
    print(f"{key:10}: {value}")

address(
  street="Johnpur Marg", 
  city="Kotdwara", 
  district="Pauri Garhwal",
  state="Uttarakhand",
  pin_code="246149"
)

# both together
def shipping_label(*args, **kwargs):
  for arg in args:
    print(arg, end=" ")
  print()

  # for value in kwargs.values():
  #   print(value)
  print(f"{kwargs.get('street')}")
  print(f"{kwargs.get('city')} {kwargs.get('district')}, {kwargs.get('state')}")
  print(f"{kwargs.get('pin_code')}")

shipping_label("Mr.", "Mayank", "Negi",
                street="Johnpur Marg", 
                city="Kotdwara", 
                district="Pauri Garhwal",
                state="Uttarakhand",
                pin_code="246149"
              )

