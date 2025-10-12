
# import os

# current_dir = os.path.dirname(__file__)

# file_path = os.path.join(current_dir, "text.txt")


# if os.path.exists(file_path):
#   print(f"The location '{file_path}' exists.")
# else:
#   print("That location doesn't exist.")

#  RECOMMENDED WAY
import os
from pathlib import Path

# If text file is in the same location.
# current_dir = Path(__file__).parent

# file_path = current_dir / 'text.txt'

# if os.path.exists(file_path):
#   print(f"The location '{file_path}' exists.")
# else:
#   print("That location doesn't exist.")

# If text file is in different location.
current_dir = Path(__file__).parent

file_path = current_dir.parent / "text_file" / "text.txt"

if os.path.exists(file_path):
  print(f"The location '{file_path}' exists.")
  if os.path.isfile(file_path):
    print("This is a file")
  elif os.path.isdir(file_path):
    print("This is a directory")

else:
  print("That location doesn't exist.")