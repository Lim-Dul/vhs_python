"""
Erste Variablen (Listen) und andere Übungen
"""
from statistics import mean
# Listen erkennen wir an eckigen Klammern. Listeneinträge werden durch Kommata getrennt.
# Hier: Die Anweisung rechts vom Gleichzeitszeichen definiert eine Liste.
# Durch die Gleichheitszeichen wird eine Variable vornamen definiert, der die Liste zugewiesen wird.
# Daher heißt diese Anweisung auch "Zuweisung".
vornamen = ["Felix", "Jan", "Christian", "Friederike", "Dirk", "Alina", "Tobias", "Dirk",
            "Irene", "Sabine", "Francisco", "Daniel"]
# Hier: Wir legen eine Liste von Integer-Werten an.
altersangaben = [29, 40, 59, 35, 31, 27, 32, 51, 44, 35, 47, 41]
orte = ["Bad Salzuflen", "Dietzenbach", "Bielefeld", "Bielefeld", "Spenge", "Bielefeld",
        "Bielefeld", "Schloss Holte-Stukenbrock", "Berlin", "Hannover", "Bielefeld", "Bielefeld"]

# print(vornamen, "Länge:", len(vornamen))
# print(altersangaben, "Länge:", len(altersangaben))
# print(orte, "Länge:", len(orte))

# # 1) Durchschnittsalter
# Kurs:
# # a) Summe der Altersangaben durch Anzahl der Altersangaben
# durchschnitt = sum(altersangaben) / len(altersangaben)
# print("Durchschnittsalter:", durchschnitt)

# # b) mean-Funktion
# durchschnitt = mean(altersangaben)
# print("Durchschnittsalter:", durchschnitt)

# # c) for-Schleife
# Summe, anzahl = 0, 0 # Alternative Doppeldeklaration

anzahl = 0
# Meine Lösung
age_sum = sum(altersangaben)
age_len = len(altersangaben)
age_avg = age_sum / age_len
print("Durchschnittsalter:", age_avg)

# 2) Häufigster Buchstage im Vornamen
first_names_concat = "".join(vornamen)
# print(first_names_concat)
first_names_unique = "".join(set(first_names_concat.lower()))
# print(first_names_unique)
# for character in first_names_unique:
#     print(character + ":", first_names_concat.lower().count(character))
char_list = []
for character in first_names_unique:
    char_list.append([character, first_names_concat.lower().count(character)])
# print(char_list)
char_list_sorted = sorted(char_list, key=lambda x: x[1], reverse=True)
# print(char_list_sorted)
for char_count_pair in char_list_sorted:
    print(char_count_pair[0] + ":", char_count_pair[1])

# 3) Häufigkeit der Wohnorte

# 4) Vornamen in alphabetisch sortierter Reihenfolge ausgeben

# 5) Altersangaben sortiert ausgeben

# 6) Vornamen nach Alter sortiert ausgeben

# 7) Vorname der jüngsten Person

# 8) Anzahl der Teilnehmenden

# 9) Anzahl unterschiedlicher Wohnorte

# 10) Häufigster Wohnort