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
for augenzahl, anzahl in sorted(strichliste.items()):
    print("Augenzahl:", augenzahl, "|", anzahl)
