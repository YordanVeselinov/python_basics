# Input
budged = float(input())
season = input()
type_vacation = ""
place = ""
expenses = 0

# Logic
if budged <= 100:
    if season == "summer":
        expenses = budged * 0.30
        type_vacation = "Camp"
        place = "Bulgaria"
    elif season == "winter":
        expenses = budged * 0.70
        type_vacation = "Hotel"
        place = "Bulgaria"
elif budged <= 1000:
    if season == "summer":
        expenses = budged * 0.40
        type_vacation = "Camp"
        place = "Balkans"
    elif season == "winter":
        expenses = budged * 0.80
        type_vacation = "Hotel"
        place = "Balkans"
elif budged > 1000:
    expenses = budged * 0.90
    type_vacation = "Hotel"
    place = "Europe"

# Output
print(f"Somewhere in {place}")
print(f"{type_vacation} - {expenses:.2f}")
