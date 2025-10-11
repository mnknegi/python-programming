# exception = An event that interrupts the flow of a program.
#             (ZeroDivisionError, TypeError, ValueError)
#             1. try 2. except 3. finally

# try:
#   Try some code
# except Exception:
#   Handle an Exception
# finally:
#   Do some clean up

try:
  number = int(input("Enter a number: "))
  print(1 / number)
except ZeroDivisionError: # 1 / 0
  print("You can't divide by zero IDIOT!")
except ValueError: # 1 / pizza
  print("Enter only numbers please!")
except Exception: # any other exception
  print("Something went wrong!")
finally:
  print("Do some cleanup here!")