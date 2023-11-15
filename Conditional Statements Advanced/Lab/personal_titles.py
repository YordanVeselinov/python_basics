# Read input
age = float(input())
gender = input().lower()
result = ""

# Logic
if gender == "m":
    if age < 16:
        result = "Master"
    else:
        result = "Mr."

elif gender == "f":
    if age < 16:
        result = "Miss"
    else:
        result = "Ms."

# Output
print(result)