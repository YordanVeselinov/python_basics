junior_cyclists = int(input())
senior_cyclists = int(input())
track_type = input()
junior_money = 0
senior_money = 0
total_people = senior_cyclists + junior_cyclists

if track_type == "trail":
    junior_money = junior_cyclists * 5.5
    senior_money = senior_cyclists * 7
elif track_type == "cross-country" and total_people < 50:
    junior_money = junior_cyclists * 8
    senior_money = senior_cyclists * 9.50
elif track_type == "downhill":
    junior_money = junior_cyclists * 12.25
    senior_money = senior_cyclists * 13.75
elif track_type == "road":
    junior_money = junior_cyclists * 20
    senior_money = senior_cyclists * 21.50
elif track_type == "cross-country" and total_people >= 50:
    junior_money = (8 * 0.75) * junior_cyclists
    senior_money = (9.50 * 0.75) * senior_cyclists


total_price = senior_money + junior_money
total_price *= 0.95

print(f"{total_price:.2f}")


