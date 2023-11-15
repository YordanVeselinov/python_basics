chrysanthemums_num = int(input())
rose_num = int(input())
tulips_num = int(input())
season = input()
day_holiday = input()

chrysanthemums_price = 0
rose_price = 0
tulips_price = 0
total_price = 0
total_num_flowers = rose_num + tulips_num + chrysanthemums_num

if season == "Spring" or season == "Summer":
    chrysanthemums_price = chrysanthemums_num * 2
    rose_price = rose_num * 4.10
    tulips_price = tulips_num * 2.50
    total_price = rose_price + tulips_price + chrysanthemums_price
elif season == "Autumn" or season == "Winter":
    chrysanthemums_price = chrysanthemums_num * 3.75
    rose_price = rose_num * 4.50
    tulips_price = tulips_num * 4.15
    total_price = rose_price + tulips_price + chrysanthemums_price

if day_holiday == "Y":
    chrysanthemums_price *= 1.15
    rose_price *= 1.15
    tulips_price *= 1.15
    total_price = rose_price + tulips_price + chrysanthemums_price

if tulips_num > 7 and season == "Spring":
    total_price *= 0.95
if rose_num >= 10 and season == "Winter":
    total_price *= 0.90
if total_num_flowers > 20:
    total_price *= 0.80

print(f"{total_price + 2:.2f}")


