
# filter(function, collection) = returns all elements that pass a condition.

# def is_passing(grade):
#   return grade >= 60

grades = [81, 92, 56, 75, 49]

# passing_grades = list(filter(is_passing, grades))

passing_grades = list(filter(lambda grade: grade >= 60, grades))

print(passing_grades)