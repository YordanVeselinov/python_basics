# Input
type_ticket = input()
rows = int(input())
columns = int(input())
total_seats = rows * columns
result = 0

# Logic
if type_ticket == "Premiere":
    result = total_seats * 12
elif type_ticket == "Normal":
    result = total_seats * 7.50
elif type_ticket == "Discount":
    result = total_seats * 5

# Output
print(f"{result:.2f} leva")

