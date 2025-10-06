
import random

low = 0
high = 10

options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"]

# number = random.randint(low, high)
# number = random.random() # random decimal number between 0 - 1.
# print(number)
option = random.choice(options)
print(option)

print(random.shuffle(cards))