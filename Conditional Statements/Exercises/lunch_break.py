from math import ceil

name_serial = input()
time_episode = int(input())
break_time = int(input())

eating = break_time * 1/8
resting = break_time * 1/4
free_for_episode = break_time - eating - resting
difference = abs(free_for_episode - time_episode)

if free_for_episode >= time_episode:
    print(f"You have enough time to watch {name_serial} and left with {ceil(difference)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_serial}, you need {ceil(difference)} more minutes.")