length = int(input())
height = int(input())
cake_pieces = length * height
taken_total = 0





user_input = input()
while user_input != "STOP":
    taken_pieces = int(user_input)
    cake_pieces -= taken_pieces
    taken_total += taken_pieces
    if cake_pieces < 0:
        break

    user_input = input()

diff = abs(cake_pieces - taken_total)

if cake_pieces > taken_pieces:
    print(f"{abs(cake_pieces)} pieces are left.")
else:
    print(f"No more cake left! You need {abs(cake_pieces)} pieces more.")


