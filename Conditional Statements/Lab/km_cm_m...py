size = int(input())
unit1 = input().lower()
unit2 = input().lower()

if unit1 == "m" :
    size = size
if unit1 == "mm" :
    size = size / 1000
if unit1 == "cm" :
    size = size / 100
if unit1 == "mi" :
    size = size / 0.000621371192
if unit1 == "in" :
    size = size / 39.3700787
if unit1 == "km" :
    size = size / 0.001
if unit1 == "ft" :
    size = size / 3.2808399
if unit1 == "yd" :
    size = size / 1.0936133
if unit2 == "m":
    size = size
    print(f"{size} {unit2}")
if unit2 == "mm":
    size = size * 1000
    print(f"{size} {unit2}")
if unit2 == "cm":
    size = size * 100
    print(f"{size} {unit2}")
if unit2 == "mi":
    size = size * 0.000621371192
    print(f"{size} {unit2}")
if unit2 == "in":
    size = size * 39.3700787
    print(f"{size} {unit2}")
if unit2 == "km":
    size = size * 0.001
    print(f"{size} {unit2}")
if unit2 == "ft":
    size = size * 3.2808399
    print(f"{size} {unit2}")
if unit2 == "yd":
    size = size * 1.0936133
    print(f"{size} {unit2}")






