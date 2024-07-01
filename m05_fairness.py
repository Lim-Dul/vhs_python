"""
Modul 05: Fairness
"""
from collections import Counter
from random import randint
import matplotlib.pyplot as plt
import numpy as np

# Ist der Würfel fair?
wuerfe = []

for i in range(1000):
    wuerfe.append(randint(1, 6))
strichliste = Counter(wuerfe)
print(sorted(strichliste.items()))
for augenzahl, anzahl in sorted(strichliste.items()):
    print("Augenzahl:", augenzahl, "|", str(round(anzahl / i, 2)) + "%")

# strichliste in zwei separate Listen entpacken (deswegen zip mit *)
x_achse, y_achse = zip(*strichliste.items())
y_achse = np.array(y_achse) / i

# Abbildung erstellen
abb = plt.figure("Fairness von Würfeln")

# Balkendiagramm erstellen
plt.bar(x_achse, y_achse)

# Beschriftung hinzufügen
plt.title("Fairness")
plt.xlabel("Augenzahl")
plt.ylabel("Prozent")

# Diagramm anzeigen
plt.show()
