puzzle_price = 2.60
doll_price = 3
bear_price = 4.10
minion_price = 8.20
truck_price = 2
vacation_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())


total_order = puzzles * puzzle_price + dolls * doll_price + bears * bear_price + minions * minion_price + trucks * truck_price
total_toys = puzzles + dolls + bears + minions + trucks
if total_toys >= 50:
     total_order =  total_order - total_order * 0.25

real_money = total_order - total_order * 0.10

if real_money >= vacation_price:
    real_money -= vacation_price
    print(f"Yes! {real_money:.2f} lv left.")
elif real_money < vacation_price:
    vacation_price -= real_money
    print(f"Not enough money! {vacation_price:.2f} lv needed.")



