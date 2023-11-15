season = input()
type_group = input()
num_students = int(input())
num_nights = int(input())

sport = "Error"
total_price = 0

if season == "Winter":
    if type_group == "boys":
        total_price = num_nights * 9.60 * num_students
        sport = "Judo"
    elif type_group == "girls":
        total_price = num_nights * 9.60 * num_students
        sport = "Gymnastics"
    elif type_group == "mixed":
        total_price = num_nights * 10 * num_students
        sport = "Ski"
elif season == "Spring":
    if type_group == "boys":
        total_price = num_nights * 7.20 * num_students
        sport = "Tennis"
    elif type_group == "girls":
        total_price = num_nights * 7.20 * num_students
        sport = "Athletics"
    elif type_group == "mixed":
        total_price = num_nights * 9.50 * num_students
        sport = "Cycling"
elif season == "Summer":
    if type_group == "boys":
        total_price = num_nights * 15 * num_students
        sport = "Football"
    elif type_group == "girls":
        total_price = num_nights * 15 * num_students
        sport = "Volleyball"
    elif type_group == "mixed":
        total_price = num_nights * 20 * num_students
        sport = "Swimming"

if 10 <= num_students < 20:
    total_price *= 0.95
elif 20 <= num_students < 50:
    total_price *= 0.85
elif num_students >= 50:
    total_price *= 0.50

print(f"{sport} {total_price:.2f} lv. ")