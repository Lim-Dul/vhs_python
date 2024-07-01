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
    i = i + 1
    print("Iteration:", i)
    kugel = randint(1, 49)
    print("Gezogen:", kugel)
    if kugel in lottozahlen:
        print("Kugel", kugel, "war schon gezogen.")
        continue
    else:
        lottozahlen.append(kugel)
        print("Lottozahlen bisher:", lottozahlen)
print("Lottozahlen für heute:", lottozahlen)

# Die Lösung mit der dummen Liste
behaelter = []
for kugel in range(1, 50):
    behaelter.append(kugel)
print(behaelter)
print("Lottozahlen für heute:", sample(behaelter, 6))