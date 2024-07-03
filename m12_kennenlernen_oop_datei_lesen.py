"""
Modul 11: Teilnehmer jetzt mit Objekten
"""
from datetime import date
from statistics import mean
import pandas as pd

class Teilnehmer:
    """
    Teilnehmer eines Kurses

    Arguments:
        object -- Objekt mit Attributen
        "vorname": str,
        "geburtsdatum": date,
        "ort": str
    """
    def __init__(self, vorname, geburtsdatum, ort):
        self.vorname = vorname
        self.geburtsdatum = geburtsdatum
        self.ort = ort

    def alter(self):
        """
        Berechnet das Alter eines Teilnehmers

        Returns:
            Alter als Int
        """
        datum = self.geburtsdatum
        heute = date.today()
        jahre = heute.year - datum.year
        if (heute.month, heute.day) < (datum.month, datum.day): # Hatte er noch nicht Geburtstag?
            jahre -= 1
        return jahre


teilnehmerliste = pd.read_csv("teilnehmer.csv", delimiter=";")
print(teilnehmerliste)

# # Vorname des zweiten Teilnehmers:
# print(teilnehmerliste[1].vorname)

# # Felix zieht um nach Frankfurt.
# print(teilnehmerliste[0].ort)
# teilnehmerliste[0].ort = "Frankfurt"
# print(teilnehmerliste[0].ort)

# # Wie alt sind Jan und Felix?
# for _ in teilnehmerliste:
#     print(_.alter())

# # Berechne das Durchschnittsalter der Teilnehmer in der teilnehmerliste:
# # a) for-Schleife
# summe_alter = 0
# anzahl_teilnehmer = len(teilnehmerliste)
# for teilnehmer in teilnehmerliste:
#     summe_alter += teilnehmer.alter()
#     durchschnitt_alter = summe_alter / anzahl_teilnehmer

# print(durchschnitt_alter)

# # b) Zwischenüberlegung: Wie bekomme ich eine Liste der Altersangaben?
# altersangaben = []
# for teilnehmer in teilnehmerliste:
#     altersangaben.append(teilnehmer.alter())

# print(sum(altersangaben) / len(altersangaben))

# # c) List comprehension (und mean)
# altersangaben = [teilnehmer.alter() for teilnehmer in teilnehmerliste]

# print(mean(altersangaben))
