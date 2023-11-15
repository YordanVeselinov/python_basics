num = int(input())
first_num = num % 10
second_num = num // 10 % 10
third_num = num // 100

for i in range(1 , first_num + 1):
    for j in range(1, second_num + 1):
        for k in range(1, third_num + 1):
            sum = i * j * k
            print(f"{i} * {j} * {k} = {sum};")
