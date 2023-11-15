from math import floor

width_ship = float(input())
length_ship = float(input())
height_ship = float(input())
average_height_astronauts = float(input())

area_ship = width_ship * height_ship * length_ship
area_astronauts = (average_height_astronauts + 0.40) * 2 * 2
astronauts = floor(area_ship / area_astronauts)

if astronauts < 3:
    print("The spacecraft is too small.")
elif 3 <= astronauts <= 10:
    print(f"The spacecraft holds {astronauts} astronauts.")
elif astronauts > 10:
    print('The spacecraft is too big.')
