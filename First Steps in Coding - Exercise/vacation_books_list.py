import math
pages = int(input())
pages_per_hour = int(input())
days = int(input())
one_hour = pages / pages_per_hour
needed_hours_per_day = one_hour / days

print(math.floor(needed_hours_per_day))