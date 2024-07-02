def is_valid(isbn):
    zahlen = list(isbn.replace("-", ""))
    if len(zahlen)!=10:
        return False
    if zahlen[-1] == "X":
        zahlen[-1] = "10"
    if not all(zahl.isdigit() for zahl in zahlen):
        return False
    return sum(int(x) * y for x, y in zip(zahlen, range(10, 0, -1))) % 11 == 0

print(is_valid("3-598-21508-8"))
