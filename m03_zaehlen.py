"""
Modul 03: Zählen
"""
from collections import Counter


satz = "Fischers Fritze fischt frische Fische"

# 1) Häufigkeit des Buschstabens "e"
# a) for-Schleife
anzahl = 0
for zeichen in satz:
    if zeichen == "e":
        anzahl += 1

print(anzahl)

# b) count-Methode des string-Objektes verwenden
print(satz.count("e"))

# 2) Übersicht der Häufigkeit für alle Zeichen / Buchstaben
# a) for-Schleife mit count-Methode, set und sorted
for zeichen in sorted(set(satz)):
    print(zeichen, satz.count(zeichen))

# b) Strichliste führen: Wörterbuch verwenden: Schlüssel=zeichen, Wert=Anzahl des Zeichens
strichliste = {} # leeres Wörterbuch
for zeichen in satz:
    if zeichen in strichliste: # zeichen zuvor schon mal gesehen, deshalb schon in strichliste
        strichliste[zeichen] += 1 # Wert in der strichliste um 1 erhöhen
    else: # zeichen haben wir noch nie gesehen, also nicht in strichliste
        strichliste[zeichen] = 1 # neuen Eintrag in der Strichliste mit Wert 1 anlegen

print(strichliste)

# c) Klasse Counter verwenden
strichliste = Counter(satz)
print(strichliste)