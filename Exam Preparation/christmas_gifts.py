user_input = input()
kid_num = 0
kid_expenses = 0
adults_num = 0
adults_expenses = 0


while user_input != "Christmas":
    age = int(user_input)
    if age <= 16:
        kid_num += 1
        kid_expenses += 5
    else:
        adults_num += 1
        adults_expenses += 15

    user_input = input()


print(f"Number of adults: {adults_num}")
print(f"Number of kids: {kid_num}")
print(f"Money for toys: {kid_expenses}")
print(f"Money for sweaters: {adults_expenses}")

