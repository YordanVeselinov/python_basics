import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

width = max(x1, x2) - min(x1, x2)
height = max(y1, y2) - min(y1, y2)

a = abs(x1-x2)
b = abs(y1-y2)

area = width * height
area = a * b

perimeter = 2 * (width+height)
perimeter = 2*a + 2*b

print("Area = ", "%.0f"% area)
print ("Area = ", math.floor(area))
print("Perimeter = ", "%.0f"% perimeter)
print("Perimeter = ", math.floor(perimeter))
