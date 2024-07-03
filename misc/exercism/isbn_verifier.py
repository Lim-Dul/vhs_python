"""
Exercism: ISBN
"""


def is_valid(isbn):
    """
    Prüft, ob eine valide ISBN-10-Nummer eingetragen wurde.
    Hierzu wird eine Checksumme aus allen Zahlen gebildet.

    Arguments:
        isbn -- Nummer im ISBN-10-Format

    Returns:
        Wahr, wenn Nummer valide
    """
    zahlen = list(isbn.replace("-", ""))
    if len(zahlen) != 10:
        return False
    if zahlen[-1] == "X":
        zahlen[-1] = "10"
    if not all(zahl.isdigit() for zahl in zahlen):
        return False
    print(zahlen)
    checksumme = 0
    for i, zahl in enumerate(zahlen):
        checksumme = checksumme + int(zahl) * (10 - i)
        # print("Multiplying", int(zahlen[i]), "by", (10 - i), "equals", int(zahlen[i]) * (10 - i))
    if checksumme % 11 == 0:
        return True
    return False

    # return sum(int(x) * y for x, y in zip(zahlen, range(10, 0, -1))) % 11 == 0

print(is_valid("3-598-21508-8"))
print(is_valid("3-598-21515-X"))
