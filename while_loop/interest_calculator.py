
principle = 0
rate = 0
time = 0

while principle <= 0:
  principle = float(input("Enter the principle amount: "))
  if principle <= 0:
    print("Principle can't be less than or equal to zero.")

while rate <= 0:
  rate = float(input("Enter the rate of interest: "))
  if rate <= 0:
    print("Rate of Interest can't be less than or equal to zero.")

while time <= 0:
  time = int(input("Enter the time: "))
  if time <= 0:
    print("Time can't be less than or equal to zero.")

print(principle)
print(rate)
print(time)

interest = principle * pow((1 + (rate/100.0)), time)
print(f"Compount Interest on {principle} with {rate} rate of interest for {time} years is {interest:.2f
                                                                                           }")