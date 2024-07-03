"""
_summary_
"""
import os
from routingpy import MapboxOSRM
from geopy.geocoders import Nominatim
from dotenv import load_dotenv

load_dotenv()

mapbox_api_key = os.getenv("MAPBOX_API_KEY")

orte = ["Bad Salzuflen", "Dietzenbach", "Bielefeld", "Bielefeld", "Spenge", "Bielefeld",
        "Bielefeld", "Schloss Holte-Stukenbrock", "Berlin", "Hannover", "Bielefeld", "Bielefeld"]

orte = set(orte)
ziel = "Bielefeld"
orte.remove(ziel)

# Define the client and their profile parameter
client = MapboxOSRM(api_key=mapbox_api_key)
profile = "driving"

# Frage: Welcher Ort aus der Menge der orte
# ist am weitesten vom ziel "VHS Bielefeld" entfernt (Luftlinie)?
geolocator = Nominatim(user_agent="vhs-bielefeld-platz11")
location = geolocator.geocode(ziel)
longlat_ziel = (location.longitude, location.latitude)
print(ziel, longlat_ziel)

distanz_orte = []
for ort in orte:
    location = geolocator.geocode(ort)
    longlat_ort = (location.longitude, location.latitude)
    print(ort, longlat_ort)
    distanz_ort = client.directions(locations=(longlat_ort, longlat_ziel), profile=profile).distance
    distanz_orte.append((distanz_ort / 1000, ort))

print(*distanz_orte, sep="\n")
print("Größte Entfernung:")
print(max(distanz_orte))
