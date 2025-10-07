
def day_of_week(day):
  match day:
    case 1:
      return "It's Sunday"
    case 2:
      return "It's Monday"
    case 3:
      return "It's Tuesday"
    case 4:
      return "It's Wednesday"
    case 5:
      return "It's Thursday"
    case 6:
      return "It's Friday"
    case 7:
      return "It's Saturday"
    case _:
      return "Not a valid day"

print(day_of_week(7))

# --------------- check weekend ---------------
def is_weekend(day):
  match day.lower():
    case "saturday" | "sunday":
      return True
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
      return False
    case _:
      return False
    
print(is_weekend("Monday"))