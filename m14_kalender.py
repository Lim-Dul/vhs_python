"""
_summary_
"""

class Kalender:
    def __init__(self, jahr, monat, tag):
        self.jahr = jahr
        self.monat = monat
        self.tag = tag

    def __repr__(self) -> str:
        return str(self.jahr) + "-" + str(self.monat) + "-" + str(self.tag)

    # def naechsterTag(self):
    #     self.tag += 1

    # def wochentag(self):

    # def iso_kalenderwoche():

    # def diff(Kalender):

k = Kalender(2024, 7, 4)
print(k)