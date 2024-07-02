"""
Modul 06: Filtern3 - Version mit Kriterium
"""


temperaturen = [-12, 5, 23, 17, 25]
vornamen = ["Anna", "Peter", "Gabi"]


def GroesserGleich20(temperatur):
    """
    Einfache Funktion zum Prüfen von Temperaturen.

    Arguments:
        temperatur -- eine Temperatur

    Returns:
        Wahr, wenn Temperatur größer oder gleich 20
    """
    return temperatur >= 20


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

print(filtern(temperaturen, GroesserGleich20))
