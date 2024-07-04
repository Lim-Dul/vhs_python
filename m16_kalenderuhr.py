"""
_summary_

Returns:
    _description_
"""
from m14_kalender import Kalender
from m15_uhr import Uhr

class KalenderUhr(Kalender, Uhr):
    def __init__(self, jahr, monat, tag, stunde, minute, sekunde):
        Kalender.__init__(self, jahr, monat, tag)
        Uhr.__init__(self, stunde, minute, sekunde)

    def __repr__(self):
        return Kalender.__repr__(self) + " " + Uhr.__repr__(self)

    def checkMitternacht(self):
        if self.stunde == 0:
            Kalender.naechsterTag(self)

    def naechsteSekunde(self):
        Uhr.naechsteSekunde(self)
        self.checkMitternacht()

ku = KalenderUhr(2024, 12, 31, 23, 59, 59)
print(ku)
ku.naechsteSekunde()
print(ku)
