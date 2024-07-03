from geopy.geocoders import Nominatim
from geopy import distance


orte = ["Bad Salzuflen", "Dietzenbach", "Bielefeld", "Bielefeld", "Spenge", "Bielefeld",
        "Bielefeld", "Schloss Holte-Stukenbrock", "Berlin", "Hannover", "Bielefeld", "Bielefeld"]

orte = set(orte)
ziel = "Bielefeld"
orte.remove(ziel)

# Frage: Welcher Ort aus der Menge der orte
# ist am weitesten vom ziel "VHS Bielefeld" entfernt (Luftlinie)?
geolocator = Nominatim(user_agent="vhs-bielefeld-platz11")
location = geolocator.geocode(ziel)
latlong_ziel = (location.latitude, location.longitude)
# print(latlong_ziel)

distanz_orte = []
for ort in orte:
    location = geolocator.geocode(ort)
    latlong_ort = (location.latitude, location.longitude)
    distanz_ort_geo = distance.distance(latlong_ort, latlong_ziel).km
    distanz_ort_gc = distance.great_circle(latlong_ort, latlong_ziel).km
    distanz_orte.append((distanz_ort_geo, distanz_ort_gc, ort))

print(*distanz_orte, sep="\n")
print("Größte Entfernung:")
print(max(distanz_orte))
