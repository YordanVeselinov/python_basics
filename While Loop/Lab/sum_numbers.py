sum_num = int(input())
sum_input = 0

while True:
    user_input = int(input())
    sum_input += user_input
    if sum_input >= sum_num:
        break



print(sum_input)