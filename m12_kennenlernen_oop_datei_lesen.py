"""
Modul 11: Teilnehmer jetzt mit Objekten
"""
from datetime import date
from statistics import mean
from dateutil import parser
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

    def to_dict(self):
        return {
            "Vorname": self.vorname,
            "Geburtsdatum": self.geburtsdatum,
            "Ort": self.ort
        }


# Pandas liest die CSV-Datei in sein eigenes internes tabellenartiges Format ein,
# das man DataFrame nennt.
dateiname = "teilnehmer.csv"
df = pd.read_csv(dateiname, sep=";")

teilnehmerliste = []
for _, teilnehmer in df.iterrows():
    datum = parser.parse(teilnehmer["Geburtsdatum"])
    teilnehmerliste.append(Teilnehmer(teilnehmer["Vorname"], datum, teilnehmer["Ort"]))

# Vorname des zweiten Teilnehmers:
print(teilnehmerliste[1].vorname)

# Felix zieht um nach Frankfurt.
idx = [teilnehmer.vorname for teilnehmer in teilnehmerliste].index("Felix")
print(teilnehmerliste[idx].ort)
teilnehmerliste[idx].ort = "Frankfurt"
print(teilnehmerliste[idx].ort)

# Abspeichern der Teilnehmer in der CSV-Datei
liste = []
for teilnehmer in teilnehmerliste:
    liste.append(teilnehmer.to_dict())

df = pd.DataFrame(liste)
df.to_csv(dateiname, sep=";", index=False)
print(df)

# Wie alt sind Jan und Felix?
for _ in teilnehmerliste:
    print(_.alter())

# Berechne das Durchschnittsalter der Teilnehmer in der teilnehmerliste:
# a) for-Schleife
summe_alter = 0
anzahl_teilnehmer = len(teilnehmerliste)
for teilnehmer in teilnehmerliste:
    summe_alter += teilnehmer.alter()
    durchschnitt_alter = summe_alter / anzahl_teilnehmer

print(durchschnitt_alter)

# b) Zwischenüberlegung: Wie bekomme ich eine Liste der Altersangaben?
altersangaben = []
for teilnehmer in teilnehmerliste:
    altersangaben.append(teilnehmer.alter())

print(sum(altersangaben) / len(altersangaben))

# c) List comprehension (und mean)
altersangaben = [teilnehmer.alter() for teilnehmer in teilnehmerliste]

print(mean(altersangaben))
