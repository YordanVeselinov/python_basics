num_locations = int(input())

for i in range(num_locations):
    average_gold = 0
    expected_average_gold_per_day = float(input())
    days_at_location = int(input())
    for i in range(days_at_location):
        gold_mined = float(input())
        average_gold += gold_mined
    average_gold /= days_at_location
    if average_gold > expected_average_gold_per_day:
        print(f"Good job! Average gold per day: {average_gold:.2f}.")
    else:
        print(f"You need {abs(average_gold - expected_average_gold_per_day):.2f} gold.")
