input_line = input()
sum_steps = 0
while input_line != "Going home":
    step = int(input_line)
    sum_steps += step
    if sum_steps >= 10000:
        break

    input_line = input()

if input_line == "Going home":
    step_home = int(input())
    sum_steps += step_home

diff = abs(sum_steps - 10000)
if sum_steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")