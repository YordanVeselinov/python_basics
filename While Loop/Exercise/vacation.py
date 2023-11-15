money_needed_for_vacation = float(input())
available_money = float(input())
days_count = 0
spending_counter = 0

while True:
    command = input()
    money = float(input())
    days_count += 1
    if command == "spend":
        spending_counter += 1
        available_money -= money
        if available_money < 0:
            available_money = 0
    elif command == "save":
        spending_counter = 0
        available_money += money

    if spending_counter == 5:
        print("You can't save the money.")
        print(days_count)
        break
    if available_money >= money_needed_for_vacation:
        print(f"You saved the money for {days_count} days.")
        break

