number_of_students = int(input())
total_grades = 0
top_students = 0
medium_students = 0
low_students = 0
fail_students = 0

for current in range(number_of_students):
    current_students_grade = float(input())
    total_grades += current_students_grade
    if current_students_grade >= 5.00:
        top_students += 1
    elif 4.00 <= current_students_grade <= 4.99:
        medium_students += 1
    elif 3.00 <= current_students_grade <= 3.99:
        low_students += 1
    elif current_students_grade < 3.00:
        fail_students += 1
print(f"Top students: {top_students / number_of_students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {medium_students / number_of_students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {low_students / number_of_students * 100:.2f}%")
print(f"Fail: {fail_students / number_of_students * 100:.2f}%")
print(f"Average: {total_grades / number_of_students:.2f}")

