"""
Modul 03: Zählen
"""
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