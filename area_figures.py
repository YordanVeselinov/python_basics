import math
type = input().lower()
num1= float(input())
area = 0.00

if type == "square":
    area = num1*num1
elif type == "rectangle":
    num2 = float(input())
    area= num1*num2
elif type == "circle":
    area= math.pi*(num1*num1)
elif type == "triangle":
    num2 = float(input())
    area= (num1*num2) / 2

print("%.3f"% area)