class VierGewinnt(object):
    def __init__(self,
                anzahl_zeilen=6,
                anzahl_spalten=7,
                spieler_symbol="X",
                computer_symbol = "O",
                leer_symbol = "."):
        self.anzahl_zeilen = anzahl_zeilen
        self.anzahl_spalten = anzahl_spalten
        self.spieler_symbol = spieler_symbol
        self.computer_symbol = computer_symbol
        self.leer_symbol = leer_symbol

        self.brett = []
        for _ in range(self.anzahl_zeilen):
            zeile = []
            for _ in range(self.anzahl_spalten):
                zeile.append(self.leer_symbol)
            self.brett.append(zeile)

    def __repr__(self):
        ausgabe = ""
        for i in range(self.anzahl_spalten):
            ausgabe += str(i) + " "
        ausgabe += "\n"
        for zeile in self.brett:
            ausgabe += " ".join(zeile) + "\n"

        return ausgabe

    def finde_freie_zeile(self, spalte):
        erfolg = False
        for zeile in reversed(range(self.anzahl_zeilen)):
            if self.brett[zeile][spalte] == self.leer_symbol:
                erfolg = True
                break

        return zeile if erfolg else None

    def spieler_zug(self):
        print(f"Du bist am Zug. Dein Symbol ist {self.spieler_symbol}.")
        while True:
            try:
                spalte = int(input("In welcher Spalte möchtest du deinen Stein setzen? "))
                if spalte in range(self.anzahl_spalten):
                    break
            except ValueError:
                pass

            print(f"Deine Angabe ist ungültig. Bitte gib eine Salte zwischen 0 und {self.anzahl_spalten - 1} ein. ")
            print(self)

        self.brett[self.finde_freie_zeile(spalte)][spalte] = self.spieler_symbol

spiel = VierGewinnt()
print(spiel)
spiel.spieler_zug()
