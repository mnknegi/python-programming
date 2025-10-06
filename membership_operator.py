
# in
# not in

# string
# word = "APPLE"

# letter = input("Guess the letter between A - Z in the secret word: ")
# if letter in word:
#   print(f"There is a {letter}.")
# else:
#   print(f"{letter} was not found.")

# set
# students = {"John", "Jane", "Joe"}
# student = input("Enter the name of the student: ")

# if student not in students:
#   print(f"{student} not found.")
# else:
#   print(f"{student} found in the list.")

# dictionary
# grades = {"Abhi": "first", "Binod": "second", "Chandini": "third", "Deepa": "fail"}

# student = input("Enter the name of the student: ")

# if student in grades:
#   print(f"{student} got {grades.get(student)} grade.")
# else:
#   print(f"No student with name {student}.")

# list
valid_email_addresses = [
  "@gmail.com",
  "@hotmail.com",
  "@yahoo.com",
  "@zoho.com",
  "@tula.com",
  "@proton.com",
]

email_address = input("Enter your email address: ")
start_index = email_address.index("@")
domain_name = email_address[start_index:]

print(domain_name)

if domain_name not in valid_email_addresses:
  print(f"{email_address} is not a valid email address.")
else:
  print(f"{email_address} is a valid email address.")