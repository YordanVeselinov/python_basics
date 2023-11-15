team = input()
type_souvenir = input()
num_souvenir = int(input())

total = 0

if team == "Argentina":
    if type_souvenir == "flags":
        total = num_souvenir * 3.25
    elif type_souvenir == "caps":
        total = num_souvenir * 7.20
    elif type_souvenir == "posters":
        total = num_souvenir * 5.10
    elif type_souvenir == "stickers":
        total = num_souvenir * 1.25
    else:
        total = "Invalid stock!"

elif team == "Brazil":
    if type_souvenir == "flags":
        total = num_souvenir * 4.20
    elif type_souvenir == "caps":
        total = num_souvenir * 8.50
    elif type_souvenir == "posters":
        total = num_souvenir * 5.35
    elif type_souvenir == "stickers":
        total = num_souvenir * 1.20
    else:
        total = "Invalid stock!"

elif team == "Croatia":
    if type_souvenir == "flags":
        total = num_souvenir * 2.75
    elif type_souvenir == "caps":
        total = num_souvenir * 6.90
    elif type_souvenir == "posters":
        total = num_souvenir * 4.95
    elif type_souvenir == "stickers":
        total = num_souvenir * 1.10
    else:
        total = "Invalid stock!"

elif team == "Denmark":
    if type_souvenir == "flags":
        total = num_souvenir * 3.10
    elif type_souvenir == "caps":
        total = num_souvenir * 6.50
    elif type_souvenir == "posters":
        total = num_souvenir * 4.80
    elif type_souvenir == "stickers":
        total = num_souvenir * 0.90
    else:
        total = "Invalid stock!"
else:
    total = "Invalid country!"

if type(total) == str:
    print(total)
else:
    print(f"Pepi bought {num_souvenir} {type_souvenir} of {team} for {total:.2f} lv.")