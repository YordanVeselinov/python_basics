from math import ceil, floor
num_santa_missing = int(input())
left_food_kg = int(input())
first_deer_food_for_one_day = float(input())
second_deer_food_for_one_day = float(input())
third_deer_food_for_one_day = float(input())


first_food = first_deer_food_for_one_day * num_santa_missing
second_food = second_deer_food_for_one_day * num_santa_missing
third_food = third_deer_food_for_one_day * num_santa_missing

total_food_needed = first_food + second_food + third_food

diff = abs(total_food_needed- left_food_kg)

if total_food_needed < left_food_kg:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")