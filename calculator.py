
operator = input("Choose any one operator (+ - * /): ")
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

if operator == "+":
  result = number1 + number2
  print(result)
elif operator == "-":
  result = number1 - number2
  print(result)
elif operator == "*":
  result = number1 * number2
  print(result)
elif operator == "/":
  result = number1 / number2
  print(result)
else:
  print(f"{operator} is not valid.")