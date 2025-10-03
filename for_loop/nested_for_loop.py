# nested loop = loop within a loop(inner, outer)
#     outer_loop:
#         inner_loop:


# for x in range(3):
#     for y in range(1, 11):
#         print(y, end="")
#     print()

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter the symbol to use: ")

for row in range(rows):
    for column in range(columns):
        print(symbol, end="")
    print()
