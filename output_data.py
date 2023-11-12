import math
volume = int(input())
pipe_1 = int(input())
pipe_2 = int(input())
hours = float(input())
water = (pipe_2 + pipe_1)*hours

if volume <= water:
    volume = math.fabs(water - volume)
    print(f"For {hours} hours the pool overflows with {volume}liters")
else:
    volume = math.trunc(water / volume * 100)
    pipe_2 = math.trunc(pipe_2 / water * 100 * hours)
    pipe_1 = math.trunc(pipe_1 / water * 100 * hours)
    print(f"The pool is {int(volume)}% full. Pipe 1: {int(pipe_1)}%. Pipe 2: {int(pipe_2)}%.")


import math
volume = int(input())
pipe_1 = int(input())
pipe_2 = int(input())
hours = float(input())
water = (pipe_2 + pipe_1)*hours

if volume <= water:
    volume = math.fabs(water - volume)
    print(f"For {hours} hours the pool overflows with {volume} liters")
else:
    volume = water / volume * 100
    pipe_2 = pipe_2 / water * 100 * hours
    pipe_1 = pipe_1 / water * 100 * hours
    print(f"The pool is {int(volume)}% full. Pipe 1: {int(pipe_1)}%. Pipe 2: {int(pipe_2)}%.")