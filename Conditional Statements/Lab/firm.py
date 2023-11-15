import math
need_hours = int(input())
days_available = int(input())
employees = int(input())
hours_lost = math.floor(employees * 10 * days_available * 0.1)
hours_available = math.floor(employees * 10 * days_available - hours_lost)
diff = math.fabs(hours_available - need_hours)


if hours_available > need_hours:
    print(f"Yes!{math.floor(diff)} hours left.")
else:
    print(f"Not enough time!{math.floor(diff)} hours needed.")
