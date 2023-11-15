# Input
volume_pool_liters = int(input())
first_pipe_hour = int(input())
second_pipe_hour = int(input())
missing_worker_hour = float(input())

# Logic

pipe_one_volume = missing_worker_hour * first_pipe_hour
pipe_two_volume = missing_worker_hour * second_pipe_hour
pipes_total = pipe_two_volume + pipe_one_volume
diff = abs((pipes_total - volume_pool_liters))
pipe_one = pipe_one_volume / pipes_total * 100
pipe_two = pipe_two_volume / pipes_total * 100
pool_full = pipes_total / volume_pool_liters * 100

if pipes_total <= volume_pool_liters:
    print(f"The pool is {pool_full:.2f}% full. Pipe 1: {pipe_one:.2f}%. Pipe 2: {pipe_two:.2f}%")
else:
    print(f"For {missing_worker_hour} hours the pool overflows with {diff:.2f} liters.")