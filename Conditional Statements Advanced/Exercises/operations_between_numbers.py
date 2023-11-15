# Input
num1 = int(input())
num2 = int(input())
operator = input()
sum = 0
odd_or_even = ""

# Logic
if operator == "/":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        sum = num1 / num2
        print(f"{num1} {operator} {num2} = {sum:.2f}")
elif operator == "+":
    sum = num1 + num2
    if sum % 2 == 0:
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
    print(f"{num1} {operator} {num2} = {sum} - {odd_or_even}")
elif operator == "*":
    sum = num1 * num2
    if sum % 2 == 0:
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
    print(f"{num1} {operator} {num2} = {sum} - {odd_or_even}")
elif operator == "-":
    sum = num1 - num2
    if sum % 2 == 0:
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
    print(f"{num1} {operator} {num2} = {sum} - {odd_or_even}")
elif operator == "%":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        sum = num1 % num2
        print(f"{num1} {operator} {num2} = {sum}")

-------------------------------------

number1 = int(input())
number2 = int(input())
operator = input()

if operator == '+' or operator == '-' or operator == '*':
    result = 0
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == '*':
        result = number1 * number2

    if result % 2 == 0:
        type_number = 'even'
    else:
        type_number = 'odd'

    print(f"{number1} {operator} {number2} = {result} - {type_number}")
elif operator == '/' and number2 != 0:
    print(f"{number1} / {number2} = {number1 / number2:.2f}")
elif operator == '%' and number2 != 0:
    print(f"{number1} % {number2} = {number1 % number2}")

if number2 == 0:
    print(f"Cannot divide {number1} by zero")