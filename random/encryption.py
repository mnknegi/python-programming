
import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
keys = chars.copy()

random.shuffle(keys)

# print(f"chars : {chars}")
# print(f"keys  : {keys}")

# ENCRYPTION
print("----------- ENCRYPTION -----------")
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
  index = chars.index(letter)
  cipher_text += keys[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

# DECRYPTION
print("----------- DECRYPTION -----------")
cipher_text = input("Enter a message to decrypt: ")
original_message = ""
for letter in cipher_text:
  index = keys.index(letter)
  original_message += chars[index]

print(f"encrypted message: {cipher_text}")
print(f"original message: {original_message}")