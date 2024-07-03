"""
Modul 11: Teilnehmer jetzt mit Objekten
"""
from datetime import date

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


t1 = Teilnehmer("Felix", date(1994, 12, 22), "Bad Salzufen")
t2 = Teilnehmer("Jan", date(1983, 12, 20), "Dietzenbach")

teilnehmerliste = [t1, t2]

# Vorname des zweiten Teilnehmers:
print(teilnehmerliste[1].vorname)

# Felix zieht um nach Frankfurt.
print(teilnehmerliste[0].ort)
teilnehmerliste[0].ort = "Frankfurt"
print(teilnehmerliste[0].ort)

# Wie alt sind Jan und Felix?
for _ in teilnehmerliste:
    print(_.alter())

# Berechne das Durchschnittsalter der Teilnehmer in der teilnehmerliste:
summe_alter = 0
anzahl_teilnehmer = 0
for teilnehmer in teilnehmerliste:
    summe_alter += teilnehmer.alter()
    durchschnitt_alter = summe_alter / anzahl_teilnehmer
print(durchschnitt_alter)
