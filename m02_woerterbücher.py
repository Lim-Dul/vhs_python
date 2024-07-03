"""
Modul 02: Wörterbücher (dictionaries)
"""
# Wörterbücher: geschweifte Klammern
# Wörterbuch-Einträge werden durch Kommata getrennt.
# Ein Wörterbuch-Eintrag ist ein Paar bestehend aus Schlüssel (key) und Wert (value).
# Hier: "Tisch" ist ein Schlüssel und "table" der dazugehörige Wert.
de_uk = {"Tisch": "table",
        "Stuhl": "chair",
        "Bier": "beer"}

# Nachschlagen eines Schlüssels im Wörterbuch über eckige Klammern.
print(de_uk["Tisch"])

# Eingabe vom Anwender über die Tastatur entgegennehmen:
wort_de = input("Bitte gib ein deutsches Wort ein: ")

# 1) LBYL: Look Before You Leap
if wort_de in de_uk: # Check: Ist wort_de ein Schlüssel im Wörterbuch de_uk?
    print("Englisch:", de_uk[wort_de])
else: # else = sonst
    print("Leider gibt es für das Wort keine Übersetzung im Wörterbuch.")

# 2) EAFP: It's Easier to Ask for Forgiveness than for Permission
try:
    print("Englisch:", de_uk[wort_de])
except KeyError:
    print("Leider gibt es für das Wort keine Übersetzung im Wörterbuch.")
