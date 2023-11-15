type_fuel = input().lower()
liters_fuel = float(input())
result = "Invalid fuel!"

if type_fuel == "diesel" or type_fuel == "gasoline" or type_fuel == "gas":
    if liters_fuel < 25:
        result = f"Fill your tank with {type_fuel}!"
    elif liters_fuel >= 25:
        result = f"You have enough {type_fuel}."

print(result)