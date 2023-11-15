

while True:
    country = input()
    current_budget = 0
    if country == "End":
        break
    needed_budget = float(input())
    while needed_budget > current_budget:
        saved_money = float(input())
        current_budget += saved_money
    if current_budget >= needed_budget:
        print(f"Going to {country}!")