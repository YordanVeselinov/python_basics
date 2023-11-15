n_birthdays = int(input())
washing_machine = float(input())
toy_price = int(input())
toy_count = 0
saved_money = 0
money_for_birthday = 10


for i in range(1, n_birthdays + 1):
    if i % 2 == 0:
        saved_money += money_for_birthday - 1
        money_for_birthday += 10

    else:
        toy_count += 1


saved_money += toy_count * toy_price

diff = abs(saved_money - washing_machine)

if saved_money >= washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")