from sys import maxsize

n = int(input())

max_num = -maxsize
sum_numbers = 0

for i in range (0, n):
    user_input = int(input())
    if user_input > max_num:
        max_num = user_input
    sum_numbers += user_input

sum_numbers -= max_num
if max_num == sum_numbers:
    print("Yes")
    print(f"Sum = {sum_numbers}")
else:
    print("No")
    print(f"Diff = {abs(sum_numbers - max_num)}")