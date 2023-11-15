num_groups = int(input())
group_1 = 0
group_2 = 0
group_3 = 0
group_4 = 0
group_5 = 0
total = 0
for i in range(num_groups):
    num_person_in_group = int(input())
    total += num_person_in_group
    if num_person_in_group <= 5:
        group_1 += num_person_in_group
    elif 6 <= num_person_in_group <= 12:
        group_2 += num_person_in_group
    elif 13 <= num_person_in_group <= 25:
        group_3 += num_person_in_group
    elif 26 <= num_person_in_group <= 40:
        group_4 += num_person_in_group
    elif num_person_in_group >= 41:
        group_5 += num_person_in_group

group_1 = group_1 / total * 100
group_2 = group_2 / total * 100
group_3 = group_3 / total * 100
group_4 = group_4 / total * 100
group_5 = group_5 / total * 100


print(f"{group_1:.2f}%")
print(f"{group_2:.2f}%")
print(f"{group_3:.2f}%")
print(f"{group_4:.2f}%")
print(f"{group_5:.2f}%")

