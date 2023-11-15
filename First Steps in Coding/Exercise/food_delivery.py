chicken_meals = int(input())
fish_meals = int(input())
vegies_meals = int(input())

chicken_price = chicken_meals * 10.35
fish_price = fish_meals * 12.40
vegies_price = vegies_meals * 8.15
total_price_food = chicken_price + fish_price + vegies_price
desert = total_price_food * 0.20
total_delivery_price = desert + total_price_food + 2.50

print(total_delivery_price)