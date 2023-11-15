length = int(input())
width = int(input())
height = int(input())
percent = int(input()) / 100

area_pool_cm = length * width * height
liters_area = area_pool_cm / 1000

needed_water = liters_area -liters_area * percent
print(needed_water)