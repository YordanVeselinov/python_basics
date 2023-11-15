from math import floor

record_sec = float(input())
record_meter = float(input())
one_meter_one_second = float(input())

time = record_meter * one_meter_one_second
time_dilay = floor(record_meter / 15) * 12.5

total_time = time_dilay + time

if total_time < record_sec:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - record_sec:.2f} seconds slower.")
