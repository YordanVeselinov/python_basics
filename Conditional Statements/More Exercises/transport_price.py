# Input
km = int(input())
day_or_night = input()

# Logic
if km < 20 and day_or_night == "night":
    km = km* 0.90 + 0.70

elif km < 20 and day_or_night == "day":
    km = km * 0.79 + 0.70

elif km >= 20 and km < 100:
    km = km * 0.09

elif km >= 100:
    km = km *0.06

# Output
print(f"{km:.2f}")
