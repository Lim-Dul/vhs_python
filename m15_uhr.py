"""
_summary_
"""

class Uhr:
    def __init__(self, stunde, minute, sekunde):
        self.stunde = stunde
        self.minute = minute
        self.sekunde = sekunde

    def __repr__(self):
        return f"{self.stunde:02d}:{self.minute:02d}:{self.sekunde:02d}"

    def naechsteSekunde(self):
        self.sekunde += 1
        if self.sekunde > 59:
            self.sekunde = 0
            self.naechsteMinute()

    def naechsteMinute(self):
        self.minute += 1
        if self.minute > 59:
            self.minute = 0
            self.naechsteStunde()

    def naechsteStunde(self):
        self.stunde += 1
        if self.stunde > 23:
            self.stunde = 0


# u = Uhr (23, 59, 59)
# print(u)
# u.naechsteSekunde()
# print(u)
# u.naechsteSekunde()
# print(u)
