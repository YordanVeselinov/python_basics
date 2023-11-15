# Input
flower = input()
num_flower = int(input())
budget = int(input())
total_cost_flowers = 0
discount = 0

# Logic
if flower == "Roses" and num_flower > 80:
    total_cost_flowers = num_flower * 5
    total_cost_flowers -= total_cost_flowers * 0.1
elif flower == "Roses":
    total_cost_flowers = num_flower * 5
elif flower == "Dahlias" and num_flower > 90:
    total_cost_flowers = num_flower * 3.80
    total_cost_flowers -= total_cost_flowers * 0.15
elif flower == "Dahlias":
    total_cost_flowers = num_flower * 3.80
elif flower == "Tulips" and num_flower > 80:
    total_cost_flowers = num_flower * 2.80
    total_cost_flowers -= total_cost_flowers * 0.15
elif flower == "Tulips":
    total_cost_flowers = num_flower * 2.80
elif flower == "Narcissus" and num_flower < 120:
    total_cost_flowers = num_flower * 3
    total_cost_flowers += total_cost_flowers * 0.15
elif flower == "Narcissus":
    total_cost_flowers = num_flower * 3
elif flower == "Gladiolus" and num_flower < 80:
    total_cost_flowers = num_flower * 2.50
    total_cost_flowers += total_cost_flowers * 0.20
elif flower == "Gladiolus":
    total_cost_flowers = num_flower * 2.50

difference = total_cost_flowers - budget

if budget >= total_cost_flowers:
    print(f"Hey, you have a great garden with {num_flower} {flower} and {abs(difference):.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(difference):.2f} leva more.")