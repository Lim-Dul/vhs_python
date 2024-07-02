"""
Modul 06: Filtern4 - Version mit lambda-Ausdrücken
"""


temperaturen = [-12, 5, 23, 17, 25]
vornamen = ["Anna", "Peter", "Gabi"]


def filtern(liste, kriterium):
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
        if kriterium(element):
            gefiltert.append(element)

    return gefiltert


# Mit lambda definiert man eine temporäre (namenlose / anonyme) Funktion
print(filtern(temperaturen, lambda temperatur: temperatur >= 20))
print(filtern(temperaturen, lambda temperatur: temperatur % 2 == 0))
