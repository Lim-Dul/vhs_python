from routingpy import MapboxOSRM
from geopy.geocoders import Nominatim
from geopy import distance

orte = ["Bad Salzuflen", "Dietzenbach", "Bielefeld", "Bielefeld", "Spenge", "Bielefeld",
        "Bielefeld", "Schloss Holte-Stukenbrock", "Berlin", "Hannover", "Bielefeld", "Bielefeld"]

orte = set(orte)
ziel = "Bielefeld"
orte.remove(ziel)

# Define the clients and their profile parameter
api = (MapboxOSRM(api_key='pk.eyJ1IjoibGltZHVsIiwiYSI6ImNseTV4NzBiczAzcjQyanNiYWl4NzVtcXUifQ.TrhWfSJ7qn3vVer_2AYEGg'), 'driving')
# Some locations in Berlin
coords = [[8.531007, 52.0191005], [8.784277, 50.0171926]]

# OSRM

client, profile = api
route = client.directions(locations=coords, profile=profile)
print(route.distance / 1000)
# print("Direction - {}:\n\tDuration: {}\n\tDistance: {}".format(client.__class__.__name__,
#                                                                 route.duration,
#                                                                 route.distance))

# # Frage: Welcher Ort aus der Menge der orte
# # ist am weitesten vom ziel "VHS Bielefeld" entfernt (Luftlinie)?
# geolocator = Nominatim(user_agent="vhs-bielefeld-platz11")
# location = geolocator.geocode(ziel)
# longlat_ziel = (location.longitude, location.latitude)
# print(longlat_ziel)

# distanz_orte = []
# for ort in orte:
#     location = geolocator.geocode(ort)
#     longlat_ort = (location.longitude, location.latitude)
#     print(ort, longlat_ort)
#     distanz_ort_geo = distance.distance(longlat_ort, longlat_ziel).km
#     distanz_ort_gc = distance.great_circle(longlat_ort, longlat_ziel).km
#     distanz_orte.append((distanz_ort_geo, distanz_ort_gc, ort))

# print(*distanz_orte, sep="\n")
# print("Größte Entfernung:")
# print(max(distanz_orte))
