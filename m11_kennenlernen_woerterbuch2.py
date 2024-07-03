"""
Modul 11: Wörterbuch als Zwischenschritt zu OOP, diesmal mit Alter
"""
from datetime import date


def alter(teilnehmer):
    """
    Berechnet das Alter eines Teilnehmers

    Arguments:
        teilnehmer -- Wörterbuch im Format {"vorname": str, "geburtsdatum": date, "ort": str}

    Returns:
        Alter als Int
    """
    datum = teilnehmer["geburtsdatum"]
    heute = date.today()
    jahre = heute.year - datum.year
    if (heute.month, heute.day) < (datum.month, datum.day): # Hatte er noch nicht Geburtstag?
        jahre -= 1
    return jahre


t1 = {"vorname": "Felix", "geburtsdatum": date(1994, 12, 1), "ort": "Bad Salzuflen"}
t2 = {"vorname": "Jan", "geburtsdatum": date(1983, 12, 20), "ort": "Dietzenbach"}

teilnehmerliste = [t1, t2]

# Wie alt sind Jan und Felix?
print(alter(teilnehmerliste[0]))
print(alter(teilnehmerliste[1]))
