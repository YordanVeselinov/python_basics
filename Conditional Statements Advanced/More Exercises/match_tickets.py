budged = float(input())
seats_class = input()
persons_in_group = int(input())

if 1 <= persons_in_group <= 4:
    budged *= 0.25
elif 5 <= persons_in_group <= 9:
    budged *= 0.40
elif 10 <= persons_in_group <= 24:
    budged *= 0.50
elif 25 <= persons_in_group <= 49:
    budged *= 0.60
elif budged >= 50:
    budged *= 0.75

money_needed_for_seats = 0

if seats_class == "VIP":
    money_needed_for_seats = persons_in_group * 499.99
else:
    money_needed_for_seats = persons_in_group * 249.99
diff = abs(money_needed_for_seats - budged)

if budged >= money_needed_for_seats:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")