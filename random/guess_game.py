
import random

low = 0
high = 100
guesses = 0
number = random.randint(low, high)

while True:
  guess = int(input(f"Enter a number between {low} - {high}: "))
  guesses += 1
  
  if guess < number:
    print(f"{guess} is too low")
  elif guess > number:
    print(f"{guess} is too high")
  else:
    print("correct guess!")
    break

print(f"You took {guesses} guesses.")