"""
Modul 06: Filtern
"""


temperaturen = [-12, 5, 23, 17, 25]

# 1) Aufgabe: Erzeuge eine neue Liste gefiltert, die nur Temperaturen >= 20 enthält.
# a) for-Schleife
gefiltert = []
for temperatur in temperaturen:
    if temperatur >= 20:
        gefiltert.append(temperatur)
print(gefiltert)

# b) List Comprehension
gefiltert = [temperatur for temperatur in temperaturen if temperatur >= 20]
print(gefiltert)

# c) filter()
def Gte20(number):
    """
    Prüft, ob Zahl größer gleich 20 ist

    Arguments:
        number -- eine Zahl

    Returns:
        Wahr, wenn größer oder gleich 20, sonst Falsch
    """
    if number >= 20:
        return True
    return False

gefiltert = list(filter(Gte20, temperaturen))
print(gefiltert)
