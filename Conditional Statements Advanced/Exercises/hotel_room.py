# Input
month = input()
nights = int(input())
studio = 0
apartment = 0

# Logic
if month == "May" or month == "October":
    if 7 < nights < 14:
        studio = (nights * 50) * 0.95
        apartment = 65 * nights
    elif nights > 14:
        studio = (nights * 50) * 0.70
        apartment = (nights * 65) * 0.90
elif month == "June" or month == "September":
    if nights > 14:
        studio = (nights * 75.20) * 0.80
        apartment = (nights * 68.70) * 0.90
    else:
        studio = nights * 75.20
        apartment = nights * 68.70
elif month == "July" or month == "August":
    if nights > 14:
        studio = nights * 76
        apartment = (nights * 77) * 0.90
    else:
        studio = nights * 76
        apartment = nights * 77

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")



