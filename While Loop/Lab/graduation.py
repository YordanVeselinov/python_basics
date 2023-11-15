name = input()
student_class = 1
average = 0
fails = 0

while True:
    grade = float(input())
    if grade < 4:
        fails += 1
        if fails >= 2:
            print(f"{name} has been excluded at {student_class} grade")
            break
        continue
    average += grade
    student_class += 1
    if student_class > 12:
        print(f"{name} graduated. Average grade: {average / 12 :.2f}")
        break