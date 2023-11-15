# Input
import math

days_left = int(input())
food_left_for_pets = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_grams = float(input())

turtle_food_kg = turtle_food_grams / 1000

total_food_needed = dog_food_kg * days_left + cat_food_kg * days_left + turtle_food_kg * days_left
diff = abs(food_left_for_pets - total_food_needed)

if total_food_needed <= food_left_for_pets:
    print(f"{math.floor(diff)} kilos of food left.")
else:
    print(f"{math.ceil(diff)} more kilos of food are needed.")