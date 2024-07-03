"""
Modul 11: Wörterbuch als Zwischenschritt zu OOP
"""
from datetime import date


vornamen = ["Felix", "Jan", "Christian", "Friederike", "Dirk", "Alina", "Tobias", "Dirk", "Irene", "Sabine", "Francisco", "Daniel"]
altersangaben = [29, 40, 59, 35, 31, 27, 32, 51, 44, 35, 47, 41]
orte = ["Bad Salzuflen", "Dietzenbach", "Bielefeld", "Bielefeld", "Spenge", "Bielefeld", "Bielefeld", "Schloss Holte-Stukenbrock", "Berlin", "Hannover", "Bielefeld", "Bielefeld"]

t1 = {"vorname": "Felix", "geburtsdatum": date(1994, 12, 1), "ort": "Bad Salzuflen"}
t2 = {"vorname": "Jan", "geburtsdatum": date(1983, 12, 20), "ort": "Dietzenbach"}

teilnehmerliste = [t1, t2]

# Vorname des zweiten Teilnehmers in der Teilnehmerliste:
print(teilnehmerliste[1]["vorname"])

# Felix zieht um nach Frankfurt.
print(teilnehmerliste[0]["ort"])
teilnehmerliste[0]["ort"] = "Frankfurt"
print(teilnehmerliste[0]["ort"])

# Wie alt ist Jan?
datum = teilnehmerliste[1]["geburtsdatum"]
heute = date.today()

alter = heute.year - datum.year
if (heute.month, heute.day) <= (datum.month, datum.day):
    alter -= 1

print(type(alter))
print(alter)
