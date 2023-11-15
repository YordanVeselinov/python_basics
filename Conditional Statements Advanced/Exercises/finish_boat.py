# Input
budget = int(input())
season = input()
fishermen = int(input())
price_ship = 0
discount = 0

# Logic
if season == "Spring":
    price_ship = 3000
elif season == "Summer" or season == "Autumn":
    price_ship = 4200
elif season == "Winter":
    price_ship = 2600

if fishermen <= 6:
    price_ship *= 0.90
elif 7 <= fishermen <= 11:
    price_ship *= 0.85
elif fishermen >= 12:
    price_ship *= 0.75

if fishermen % 2 == 0 and season != "Autumn":
    price_ship *= 0.95

difference = budget - price_ship

if budget >= price_ship:
    print(f"Yes! You have {abs(difference):.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(difference):.2f} leva.")
