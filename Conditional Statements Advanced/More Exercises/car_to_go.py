budget = float(input())
season = input()
car_class = "Error"
car_type = "Error"

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        budget *= 0.35
        car_type = "Cabrio"
    elif season == "Winter":
        budget *= 0.65
        car_type = "Jeep"
elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        budget *= 0.45
        car_type = "Cabrio"
    elif season == "Winter":
        budget *= 0.80
        car_type = "Jeep"
elif budget > 500:
    car_class = "Luxury class"
    budget *= 0.90
    car_type = "Jeep"

print(f"{car_class}")
print(f"{car_type} - {budget:.2f}")