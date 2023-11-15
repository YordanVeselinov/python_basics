num_tabs = int(input())
salary = int(input())

fine = 0

for i in range(num_tabs):
    name_website = input()
    if name_website == "Facebook":
        fine += 150
    elif name_website == "Instagram":
        fine += 100
    elif name_website == "Reddit":
        fine += 50
    if fine >= salary:
        break

diff = abs(salary - fine)

if fine >= salary:
    print("You have lost your salary.")
else:
    print(diff)