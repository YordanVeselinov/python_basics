# Output
fruit = input()
day = input()
qty = float(input())
result = "error"

# Logic
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        result = qty * 2.50
    elif fruit == "apple":
        result = qty * 1.20
    elif fruit == "orange":
        result = qty * 0.85
    elif fruit == "grapefruit":
        result = qty * 1.45
    elif fruit == "kiwi":
        result = qty * 2.70
    elif fruit == "pineapple":
        result = qty * 5.50
    elif fruit == "grapes":
        result = qty * 3.85
elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        result = qty * 2.70
    elif fruit == "apple":
        result = qty * 1.25
    elif fruit == "orange":
        result = qty * 0.90
    elif fruit == "grapefruit":
        result = qty * 1.60
    elif fruit == "kiwi":
        result = qty * 3
    elif fruit == "pineapple":
        result = qty * 5.60
    elif fruit == "grapes":
        result = qty * 4.20



# Output
if result == "error":
    print(result)
else:
    print(f"{result:.2f}")