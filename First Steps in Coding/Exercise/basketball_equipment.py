tax_for_year = int(input())
shoes = tax_for_year - tax_for_year * 0.40
outfit = shoes - shoes * 0.20
ball = outfit / 4
accessories = ball / 5

total_cost = shoes + outfit + ball + accessories + tax_for_year
print(total_cost)