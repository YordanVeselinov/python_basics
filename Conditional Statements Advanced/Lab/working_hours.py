# Input
hours = int(input())
day = input()
result = "closed"

# Logic
if day != "Sunday":
    if 10 <= hours <= 18:
        result = "open"


# Output
print(result)