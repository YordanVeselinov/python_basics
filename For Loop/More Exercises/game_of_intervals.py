turns = int(input())
total_points = 0
from_zero_to_tine = 0
from_ten_to_nineteen = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid = 0
total_grades = 0
for _ in range(turns):
    points = int(input())
    if 0 <= points <= 9:
        from_zero_to_tine += 1
        total_points += points * 0.20
    elif 10 <= points <= 19:
        from_ten_to_nineteen += 1
        total_points += points * 0.30
    elif 20 <= points <= 29:
        from_20_to_29 += 1
        total_points += points * 0.40
    elif 30 <= points <= 39:
        from_30_to_39 += 1
        total_points += 50
    elif 40 <= points <= 50:
        from_40_to_50 += 1
        total_points += 100
    else:
        invalid += 1
        total_points /= 2
    total_grades += 1
print(f"{total_points:.2f}")
print(f"From 0 to 9: {from_zero_to_tine / total_grades * 100:.2f}%")
print(f"From 10 to 19: {from_ten_to_nineteen / total_grades * 100:.2f}%")
print(f"From 20 to 29: {from_20_to_29 / total_grades * 100:.2f}%")
print(f"From 30 to 39: {from_30_to_39 / total_grades * 100:.2f}%")
print(f"From 40 to 50: {from_40_to_50 / total_grades * 100:.2f}%")
print(f"Invalid numbers: {invalid / total_grades * 100:.2f}%")
