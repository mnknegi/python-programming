
def net_price(list_price, discount=0, tax=0.05):
  return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0, 0.05))
print(net_price(500))

print(net_price(500, 0.1)) # (list_price, discount, tax=0.05)

import time

# def count(start=0, end) default arguments should follow non-default argument.
def count(end, start=0):
  for second in range(start, end+1):
    print(second)
    time.sleep(1)
  print("Done")

# count(10, 5)
count(10)