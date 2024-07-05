import random


class VierGewinnt(object):
    def __init__(self, anzahl_zeilen=6, anzahl_spalten=7, spieler_symbol="X", computer_symbol="O", leer_symbol="."):
        self.anzahl_zeilen = anzahl_zeilen
        self.anzahl_spalten = anzahl_spalten
        self.spieler_symbol = spieler_symbol
        self.computer_symbol = computer_symbol
        self.leer_symbol = leer_symbol

        self.brett = []
        for i in range(anzahl_zeilen):
            zeile = []
            for j in range(anzahl_spalten):
                zeile.append(leer_symbol)
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
                spalte = int(input("In welcher Spalte möchtest Du Deinen Stein setzen? "))
                if spalte in range(self.anzahl_spalten) and self.finde_freie_zeile(spalte) is not None:
                    break
            except ValueError:
                pass

            print(f"Deine Eingabe ist ungültig. Bitte gib eine Spalte zwischen 0 und {self.anzahl_spalten - 1} ein.")
            print(self)

        self.brett[self.finde_freie_zeile(spalte)][spalte] = self.spieler_symbol

    def computer_zug(self):
        gueltige_spalten = [spalte for spalte in range(self.anzahl_spalten) if self.finde_freie_zeile(spalte) is not None]
        spalte = random.choice(gueltige_spalten)
        self.brett[self.finde_freie_zeile(spalte)][spalte] = self.computer_symbol

    def hat_gewonnen(self, symbol):
        # horizontal
        for zeile in self.brett:
            zeile_str = "".join(zeile)
            try:
                if zeile_str.index(symbol * 4) >= 0:
                    return True
            except ValueError:
                pass

        # vertikal
        for spalte in range(self.anzahl_spalten):
            spalte_str = "".join(zeile[spalte] for zeile in self.brett)
            try:
                if spalte_str.index(symbol * 4) >= 0:
                    return True
            except ValueError:
                pass

        # diagonal: TODO

        return False

    def start_spiel(self):
        while True:
            print(self)  # Spielbrett anzeigen
            self.spieler_zug()  # Nächster Zug: Spieler
            if self.hat_gewonnen(self.spieler_symbol):
                print(self) # Spielbrett anzeigen
                print("Du hast gewonnen!")
                return
            self.computer_zug() # Nächster Zug: Computer
            if self.hat_gewonnen(self.computer_symbol):
                print(self) # Spielbrett anzeigen
                print("Ätsch, ich habe gewonnen!")
                return


spiel = VierGewinnt()
spiel.start_spiel()

# TODO: Wenn Brett voll, aber keine 4er, dann unentschieden
