"""
Modul 11: Teilnehmer jetzt mit Objekten
"""
import json
from datetime import date
from dateutil import parser


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

    def __repr__(self):
        return f"{self.vorname}, {str(self.geburtsdatum)}, {self.ort}"

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
        return {"vorname": self.vorname,
                "geburtsdatum": str(self.geburtsdatum),
                "ort": self.ort}

    @staticmethod
    def from_dict(d):
        return Teilnehmer(d["vorname"], parser.parse(d["geburtsdatum"]), d["ort"])


t1 = Teilnehmer("Felix", date(1994, 12, 22), "Bad Salzufen")
t2 = Teilnehmer("Jan", date(1983, 12, 20), "Dietzenbach")

teilnehmerliste = [t1, t2]

with open("m25_teilnehmer.json", "w", encoding="utf-8") as datei:
    json.dump([teilnehmer.to_dict() for teilnehmer in teilnehmerliste], datei, indent=4)

print(teilnehmerliste)

with open("m25_teilnehmer.json", "r", encoding="utf-8") as datei:
    objekt = json.load(datei)
    teilnehmerliste = []
    for d in objekt:
        teilnehmerliste.append(Teilnehmer.from_dict(d))

print(teilnehmerliste)
