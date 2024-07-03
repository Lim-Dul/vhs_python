from geopy.geocoders import Nominatim


orte = ["Bad Salzuflen", "Dietzenbach", "Bielefeld", "Bielefeld", "Spenge", "Bielefeld",
        "Bielefeld", "Schloss Holte-Stukenbrock", "Berlin", "Hannover", "Bielefeld", "Bielefeld"]

orte = set(orte)
ziel = "VHS Bielefeld"

# Frage: Welcher Ort aus der Menge der orte
# ist am weitesten vom ziel "VHS Bielefeld" entfernt (Luftlinie)?
