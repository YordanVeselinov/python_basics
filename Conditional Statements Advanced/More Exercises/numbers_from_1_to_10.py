from sys import maxsize
n = maxsize
for i in range(n):
    user_input = float(input())
    result = user_input * 2
    if result >= 0:
        print(f"Result: {result:.2f}")
    else:
        print("Negative number!")
        break
