num_persons = int(input())
season = input()
price = 0

if num_persons <= 5:
    if season == "spring":
        price = num_persons * 50
    elif season == "summer":
        price = num_persons * 48.50
        price *= 0.85
    elif season == "autumn":
        price = num_persons * 60
    elif season == "winter":
        price = num_persons * 86
        price *= 1.08
elif num_persons > 5:
    if season == "spring":
        price = num_persons * 48
    elif season == "summer":
        price = num_persons * 45
        price *= 0.85
    elif season == "autumn":
        price = num_persons * 49.50
    elif season == "winter":
        price = num_persons * 85
        price *= 1.08

print(f"{price:.2f} leva.")
