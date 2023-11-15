budget = float(input())
season = input()
country = "Error"
place = "Error"

if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        budget *= 0.65
        country = "Alaska"
    elif season == "Winter":
        budget *= 0.45
        country = "Morocco"
elif 1000 < budget <= 3000:
    place = "Hut"
    if season == "Summer":
        budget *= 0.80
        country = "Alaska"
    elif season == "Winter":
        budget *= 0.60
        country = "Morocco"
elif budget > 3000:
    place = "Hotel"
    budget *= 0.90
    if season == "Summer":
        country = "Alaska"
    elif season == "Winter":
        country = "Morocco"

print(f"{country} - {place} - {budget:.2f}")