price_kg_vegetables = float(input())
price_kg_fruit = float(input())
total_kg_vegetables = int(input())
total_kg_fruit = int(input())

profit_vegetables = price_kg_vegetables * total_kg_vegetables
profit_fruit = price_kg_fruit* total_kg_fruit
profit_total_bgn = profit_fruit + profit_vegetables
profit_eur = profit_total_bgn / 1.94
print(f"{profit_eur:.2f}")
