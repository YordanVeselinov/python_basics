budget_film = float(input())
number_extras = int(input())
budget_one_extras = float(input())
decor = 0
decor = budget_film * 10/100

if number_extras > 150:
    budget_one_extras *= number_extras
    budget_one_extras -= budget_one_extras * 0.10
else:
    budget_one_extras *= number_extras

total_expenses = budget_one_extras + decor

if budget_film < total_expenses:
    difference = total_expenses - budget_film
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
elif budget_film >= total_expenses:
    difference = budget_film - total_expenses
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
