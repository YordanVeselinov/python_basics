type_fuel = input()
fuel_liters = float(input())
card = input()
total_cost = 0.0

if card == "Yes":
    price_gas = 0.93 - 0.08
    price_diesel = 2.33 - 0.12
    price_gasoline = 2.22 - 0.18
else:
    price_gas = 0.93
    price_diesel = 2.33
    price_gasoline = 2.22

if type_fuel == "Diesel":
    total_cost = price_diesel * fuel_liters
elif type_fuel == "Gas":
    total_cost = price_gas * fuel_liters
elif type_fuel == "Gasoline":
    total_cost = price_gasoline * fuel_liters

if 20 < fuel_liters <= 25:
    total_cost *= 0.92
elif  fuel_liters > 25:
    total_cost *= 0.90

print(f"{total_cost:.2f} lv.")



