wanted_book = input()
count_books = 0

while True:
    books = input()
    if books == wanted_book:
        print(f"You checked {count_books} books and found it.")
        break

    if books == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {count_books} books.")
        break
    count_books += 1