# Input
nights = int(input()) - 1
type_room = input()
rating = input()

one_person = nights * 18
apartment = nights * 25
president = nights * 35

# Logic
if nights < 10:
    apartment *= 0.70
    president *= 0.90
elif 10 <= nights <= 15:
    apartment *= 0.65
    president *= 0.85
elif nights > 15:
    apartment *= 0.50
    president *= 0.80

if rating == "positive":
    one_person += one_person * 0.25
    apartment += apartment * 0.25
    president += president * 0.25
else:
    one_person *= 0.90
    apartment *= 0.90
    president *= 0.90

# Output
if type_room == "room for one person":
    print(f"{one_person:.2f}")
elif type_room == "apartment":
    print(f"{apartment:.2f}")
elif type_room == "president apartment":
    print(f"{president:.2f}")