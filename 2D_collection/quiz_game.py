
questions = ("How many elements are in the perodic table?: ",
             "which animal lays the largest egg?: ",
             "What is the most abundant gas in the Earth's atmosphere?: ",
             "How many bones are in human body?: ",
             "which planet in the solar system is the hottest?: "
             )

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")

gussess = []
score = 0
question_number = 0

for question in questions:
  print("-------------------------")
  print(question)
  for option in options[question_number]:
    print(option)
    
  guess = input("Enter (A, B, C, D): ").upper()
  if guess == answers[question_number]:
    print("Correct")
    score += 1
  else:
    print("Incorrect")
    print(f"Correct answer is {answers[question_number]}")
  question_number += 1
  gussess.append(guess)

print("-------------------------")
print("          RESULT         ")
print("-------------------------")

for answer in answers:
  print(answer, end=" ")
print()

for guess in gussess:
  print(guess, end=" ")
print()

score = score / len(questions) * 100
print(f"Your score is: {score}")