def is_valid(isbn):
    if len(isbn) != 13:
        print("WTF?")
    if isbn[1] and isbn[5] and isbn[11] != "-":
        print("WTF?")
    processed = isbn.replace()
    processed = list(isbn)
    print(processed)

is_valid("3-598-21508-8")