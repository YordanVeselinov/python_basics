days = int(input())
treated_patients = 0
untreated_patients = 0
doctors = 7
for current_day in range(1, days+1):
    patients = int(input())
    if current_day % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1
    if patients >= doctors:
        treated_patients += doctors
        untreated_patients += patients - doctors
    else:
        treated_patients += patients
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")

