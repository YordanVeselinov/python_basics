nylon = int(input())
paint = int(input())
paint_thinner = int(input())
hours = int(input())

price_nylon = (nylon + 2)* 1.50
price_paint = (paint +paint* 0.10) * 14.50
price_thinner = paint_thinner * 5
price_total = 0.40 +price_thinner + price_paint + price_nylon
money_for_workman = (price_total * 0.30) * hours
total = price_total + money_for_workman
print(total)
