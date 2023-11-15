name_of_actor = input()
point_from_academy = float(input())
num_jury = int(input())
total_points = point_from_academy

for i in range (num_jury):
    name_jury = input()
    rating_jury = (float(input()) * len(name_jury) )/2
    total_points += rating_jury
    if total_points > 1250.5:
        break


diff = abs(total_points - 1250.5)
if total_points < 1250.5:
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")
else:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
