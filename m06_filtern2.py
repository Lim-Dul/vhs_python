"""
Modul 06: Filtern2 - Versionen von filtern()
"""


temperaturen = [-12, 5, 23, 17, 25]
vornamen = ["Anna", "Peter", "Gabi"]


def filtern(liste, lb):
    """
    Iteriert über eine Liste von Elementen und prüft, ob ein Element größer als 20 ist.

    Arguments:
        liste -- Liste von Zahlen
        lb -- Lower Bound
    Returns:
        Eine neue Liste, die nur Zahlen, die größer als 20 sind, enthält.
    """
    gefiltert = []
    for element in liste:
        if element >= lb:
            gefiltert.append(element)

    return gefiltert

print(filtern(temperaturen, 20))
print(filtern(temperaturen, 10))
print(filtern(vornamen, "G"))
