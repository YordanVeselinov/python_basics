capicity_of_stadiom = int(input())
number_of_fans = int(input())
a_section = 0
b_section = 0
v_section = 0
g_section = 0

for current_fan in range(number_of_fans):
    section = input()
    if section == "A":
        a_section += 1
    elif section == "B":
        b_section += 1
    elif section == "V":
        v_section += 1
    elif section == "G":
        g_section += 1

print(f"{a_section / number_of_fans * 100:.2f}%")
print(f"{b_section / number_of_fans * 100:.2f}%")
print(f"{v_section / number_of_fans * 100:.2f}%")
print(f"{g_section / number_of_fans * 100:.2f}%")
print(f"{number_of_fans / capicity_of_stadiom * 100:.2f}%")