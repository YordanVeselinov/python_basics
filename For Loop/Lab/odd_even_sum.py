# Input
n = int(input())
even_sum = 0
odd_sum = 0

# Logic
for i in range(n):
    user_input = int(input())
    if i % 2 == 0:
        even_sum += user_input
    else:
        odd_sum += user_input

diff = abs(odd_sum - even_sum)

# Output
if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    print("No")
    print(f"Diff = {diff}")
