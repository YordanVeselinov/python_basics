from math import ceil
price_video_card = int(input())
transition_price = int(input())
price_electricity_day = float(input())
profit_video_card_day = float(input())


video_card = price_video_card * 13
transition = transition_price * 13
total_expenses = video_card + transition + 1000
profit_per_day = abs(profit_video_card_day - price_electricity_day) * 13

days_needed = total_expenses / profit_per_day

print(f"{total_expenses}")
print(f"{ceil(days_needed)}")
