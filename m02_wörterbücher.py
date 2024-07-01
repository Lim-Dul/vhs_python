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