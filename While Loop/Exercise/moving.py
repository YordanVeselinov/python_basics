width_apartment = int(input())
length_apartment = int(input())
height_apartment = int(input())
cubic_apartment = width_apartment * length_apartment * height_apartment
total_cubic_cartos = 0
user_input = input()

while user_input != "Done":
    cubic_cartons = int(user_input)
    total_cubic_cartos += cubic_cartons
    if total_cubic_cartos > cubic_apartment:
        break
    user_input = input()

diff = abs(total_cubic_cartos - cubic_apartment)

if total_cubic_cartos > cubic_apartment:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")