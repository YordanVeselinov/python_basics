import math
vineyard_area = int(input())
grape_per_square = float(input())
needed_liter = float(input())
workers = int(input())
wine = ((vineyard_area * 0.4) * grape_per_square ) / 2.5
diff = math.fabs(wine - needed_liter)
wine_per_person = diff / workers

if wine < needed_liter:
    print(f"It will be a tough winter! More {math.floor(diff)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    print(f"{math.ceil(diff)} liters left -> {math.ceil(wine_per_person)} liters per person.")


