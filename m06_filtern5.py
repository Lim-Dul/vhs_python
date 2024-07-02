"""
Modul 06: Filtern5 - Version mit filter()
"""


def GroesserGleich20(temperatur):
    """
    Einfache Funktion zum Prüfen, ob Temperatur größer als oder gleich 20 ist.

    Arguments:
        temperatur -- eine Temperatur

    Returns:
        Wahr, wenn Temperatur größer oder gleich 20
    """
    return temperatur >= 20

temperaturen = [-12, 5, 23, 17, 25]
vornamen = ["Anna", "Peter", "Gabi"]

# Mit lambda definiert man eine temporäre (namenlose / anonyme) Funktion
print(filter(temperaturen, GroesserGleich20))
print(filter(temperaturen, lambda temperatur: temperatur >= 20))
print(filter(temperaturen, lambda temperatur: temperatur % 2 == 0))
