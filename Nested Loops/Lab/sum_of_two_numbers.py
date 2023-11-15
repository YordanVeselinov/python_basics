start_number = int(input())
end_number = int(input())
magic_number = int(input())
number_of_combination = 0
magic_number_is_found = False

for first in range(start_number, end_number + 1):
    for second in range(start_number, end_number + 1):
        number_of_combination += 1
        if first + second == magic_number:
            magic_number_is_found = True
            break
    if magic_number_is_found:
        break
if magic_number_is_found:
    print(f'Combination N:{number_of_combination} ({first} + {second} = {magic_number})')
else:
    print(f"{number_of_combination} combinations - neither equals {magic_number}")