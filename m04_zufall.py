"""
Modul 04: Zufallszahlen
"""
from random import randint, sample


# augenzahl = randint(1, 6)
# print(augenzahl)

# Lotto-Ziehung "6 aus 49"
# Schreibe ein Programm, das 6 verschiedene zufällige 
lottozahlen = []
i = 0
while len(lottozahlen) < 6:
    # i = i + 1 # Hilfsvariable zur Iterations-Zählung
    # print("Iteration:", i)
    kugel = randint(1, 49) # Zufällige Zahl generieren
    # print("Gezogen:", kugel)
    if kugel in lottozahlen: # Check, ob sie schon einmal gezogen wurde
        # print("Kugel", kugel, "war schon gezogen.")
        continue # Einfach nix machen (nächste Iteration)
    else:
        lottozahlen.append(kugel) # Zahl in die Liste aufnehmen
        # print("Lottozahlen bisher:", lottozahlen)
print("Lottozahlen für heute:", lottozahlen)

# Die Lösung mit der dummen Liste
behaelter = list(range(1, 50)) # Mit 49 Kugeln befüllen (warum ist die Range nach oben offen PYTHON??????)
print(behaelter)
print("Lottozahlen für heute:", sample(behaelter, 6)) # Mit Funktion sample 6 Elemente ohne Wiederholungen ziehen