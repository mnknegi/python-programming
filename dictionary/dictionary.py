
capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "Sri Lanka": "Colombo",
            "UK": "London",
            "France": "Paris"
            }

# print(dir(capitals))
# for capital in capitals.values():
#   print(capital)

# print(capitals["USA"]) // not safe. Excaption if key not find. Use 'get()' instead.

# if capitals.get("Japan"):
#   print("Capital for this country exists.")
# else:
#   print("Capital for this country don't exist.")

# capitals.update({"Germany": "Berlin"})

# print(capitals.get("Germany"))

# capitals["Bangladesh"] = "Dhaka"

# print(capitals.pop("Bangladesh")) // This will throw an exception if Bangladesh key is not present.
# print(capitals.pop("Bangladesh", "Not Found")) # To avoid the exception, provide a default value.

# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for key, value in capitals.items():
  print(f"{key} - {value}")