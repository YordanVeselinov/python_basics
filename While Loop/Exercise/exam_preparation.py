num_failed_grates = int(input())
failed_grades = 0
average_grade = 0
solved_grades = 0
last_problem = ""

while True:
    name_problem = input()
    if name_problem == "Enough":
        print(f"Average score: {average_grade / solved_grades:.2f}")
        print(f"Number of problems: {solved_grades}")
        print(f"Last problem: {last_problem}")
        break
    grate = int(input())
    average_grade += grate
    solved_grades += 1
    if grate <= 4:
        failed_grades += 1
    last_problem = name_problem
    if failed_grades == num_failed_grates:
        print(f"You need a break, {failed_grades} poor grades.")
        break


