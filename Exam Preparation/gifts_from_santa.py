n = int(input())
m = int(input())
s = int(input())

for i in range (m, n, -1):
    if i % 2 == 0 and i % 3 == 0 and i == s:
        break
    elif i % 3 == 0 and i % 2 == 0:
        print(i, end=' ')
