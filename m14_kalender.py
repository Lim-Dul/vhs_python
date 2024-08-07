"""
_summary_
"""

class Kalender:
    def __init__(self, jahr, monat, tag):
        self.jahr = jahr
        self.monat = monat
        self.tag = tag

    def __repr__(self):
        # return str(self.jahr) + "-" + str(self.monat) + "-" + str(self.tag)
        # return "%04i-%02i-%02i" % (self.jahr, self.monat, self.tag)
        return f"{self.jahr:04d}-{self.monat:02d}-{self.tag:02d}"

    def ist_schaltjahr(self):
        return self.jahr % 400 == 0 or (self.jahr % 100 != 0 and self.jahr % 4 == 0)

    TAGE_PRO_MONAT = (None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def naechsterTag(self):
        self.tag += 1

        if self.ist_schaltjahr() and self.monat == 2:
            korrektur = 1
        else:
            korrektur = 0

        if self.tag > Kalender.TAGE_PRO_MONAT[self.monat] + korrektur:
            self.tag = 1
            self.naechsterMonat()

    def naechsterMonat(self):
        self.monat += 1
        if self.monat > 12:
            self.monat = 1
            self.naechstesJahr()

    def naechstesJahr(self):
        self.jahr += 1

    # def wochentag(self):

    # def iso_kalenderwoche():

    # def diff(Kalender):

# k = Kalender(2024, 2, 28)
# print(k)
# k.naechsterTag()
# print(k)
# k = Kalender(2024, 12, 31)
# print(k)
# k.naechsterTag()
# print(k)
