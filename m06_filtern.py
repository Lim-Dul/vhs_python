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

# c) Eigene Funktion filter definieren
# Das Schlüsselwort def leitet die Definition einer neuen Funktion ein.
# Die Funktion hat einen Namen. Hier: filter
# Auf den Namen folgt ein Paar runder Klammern,
# in dem ggf. sogenannte Parameter / Argumente definiert werden.
# Der Doppelpunkt leitet den nachfolgenden Block ein, in dem die Implementierung der Funktion steht.
def filtern(liste):
    """
    Iteriert über eine Liste von Elementen und prüft, ob ein Element größer als 20 ist.

    Arguments:
        liste -- Liste von Zahlen

    Returns:
        Eine neue Liste, die nur Zahlen, die größer als 20 sind, enthält.
    """
    gefiltert_f = []
    for element in liste:
        if element >= 20:
            gefiltert_f.append(element)

    return gefiltert_f

print(filtern(temperaturen))

# Meine Lösung
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

gefiltert = filter(Gte20, temperaturen)
print(gefiltert) # Funktioniert nicht wie man denkt
print(type(gefiltert)) # Was ist denn "gefiltert"? Ein Objekt!
# Loop funktioniert dann wie man denkt ;)
for x in gefiltert:
    print(x)
# Sonst auf Liste casten
gefiltert = list(filter(Gte20, temperaturen))
print(gefiltert)
