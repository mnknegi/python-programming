# format specifiers: {:flags} format a value based on what flags are inserted.

price1 = 3.14798
price2 = -987.12
price3 = 12.87

print(f"price 1 is: ${price1:.2f}")
print(f"price 2 is: ${price2:.1f}")
print(f"price 3 is: ${price3:.3f}")

# spacing before numbers
print(f"price 1 is: ${price1:10}")
print(f"price 2 is: ${price2:10}")
print(f"price 3 is: ${price3:10}")

# zero padded
print(f"price 1 is: ${price1:010}")
print(f"price 2 is: ${price2:010}")
print(f"price 3 is: ${price3:010}")

# left justify a value(left angle bracket)
print(f"price 1 is: ${price1:<10}")
print(f"price 2 is: ${price2:<10}")
print(f"price 3 is: ${price3:<10}")

# right justify a value(right angle bracket)
print(f"price 1 is: ${price1:>10}")
print(f"price 2 is: ${price2:>10}")
print(f"price 3 is: ${price3:>10}")

# centre align(caret sign)
print(f"price 1 is: ${price1:^10}")
print(f"price 2 is: ${price2:^10}")
print(f"price 3 is: ${price3:^10}")

# to show positive value, use +
print(f"price 1 is: ${price1:+}")
print(f"price 2 is: ${price2:+}")
print(f"price 3 is: ${price3:+}")

# thousand separator
price4 = 243500.03495
print(f"price 4 is: {price4:,}")

# mix multiple separators
print(f"price 4 is: {price4:+,.2f}")