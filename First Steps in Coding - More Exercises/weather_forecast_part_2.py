degrees = float(input())
result = "unknown"

if 26 <= degrees <= 35:
    result = "Hot"
elif 20.1 <= degrees <= 25.9:
    result = "Warm"
elif 15 <= degrees <= 20:
    result = "Mild"
elif 12 <= degrees <= 14.9:
    result = "Cool"
elif 5 <= degrees <= 11.9:
    result = "Cold"

print(result)