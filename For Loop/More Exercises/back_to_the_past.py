inheritance = float(input())
year = int(input())
spend = 0
old = 18
for current_year in range(1800, year + 1):
    if current_year % 2 == 0:
        spend = 12000

    elif current_year % 2 != 0:
        spend = 12000 + old*50
    old += 1
    inheritance -= spend


if inheritance >= 0:
    print(f"Yes! He will live a carefree life and will have {inheritance:.2f} dollars left.")
else:
    print(f'He will need {abs(inheritance):.2f} dollars to survive.')

