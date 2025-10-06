
import random

options = ("rock", "paper", "scissors")
running = True

while running:

  player = None
  computer = random.choice(options)

  while player not in options:
    player = input("Enter a choice (rock, paper, scissors): ")

  print(f"{player}")
  print(f"{computer}")
  
  if player == computer:
    print("it's a tie!")
  elif player == "rock" and computer == "scissors":
    print("You win!")
  elif player == "paper" and computer == "rock":
    print("You win!")
  elif player == "scissors" and computer == "paper":
    print("You win!")
  else:
    print("Computer win!")

  if not input("Play again (y/n): ").lower() == "y":
    running = False

print("Thanks for playing!")