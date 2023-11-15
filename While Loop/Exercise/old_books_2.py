# Input
wanted_book = input()
count_books = 0
current_book = input()
is_book_fount = False

# Loop
while current_book != "No More Books":
    if current_book == wanted_book:
        is_book_fount = True
        break
    count_books += 1
    current_book = input()

# Output
if is_book_fount:
    print(f"You checked {count_books} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {count_books} books.")