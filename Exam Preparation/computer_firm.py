num_pc = int(input())
rating_num = 0
rating_count = 0
total_sum = 0
for i in range(num_pc):
    user_input = int(input())
    rating = user_input % 10
    price = user_input // 10
    if rating == 2:
        price = 0
    elif rating == 3:
        price = price * 0.50
    elif rating == 4:
        price = price * 0.70
    elif rating == 5:
        price = price * 0.85
    elif rating == 6:
        price = price
    total_sum += price
    rating_count += 1
    rating_num += rating
average_rating = rating_num / rating_count

print(f"{total_sum:.2f}")
print(f"{average_rating:.2f}")

