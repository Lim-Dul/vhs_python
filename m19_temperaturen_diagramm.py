import datetime
import matplotlib.pyplot as plt
from geopy import Nominatim
from metno_locationforecast import Place, Forecast

ort = "Bielefeld"
agent = "vhs-bielefeld-platz11"

# Geopy
geolocator = Nominatim(user_agent=agent)
location = geolocator.geocode(ort)

# Metno
place = Place(ort, latitude=location.latitude, longitude=location.longitude)
forecast = Forecast(place, agent)
forecast.update()

# Listen fürs Plotten vorbereiten
times = []
temperatures = []

for interval in forecast.data.intervals_for(datetime.date.today()):
    times.append(interval.start_time.hour)
    temperatures.append(interval.variables["air_temperature"].value)

# Erstelle das Liniendiagramm
plt.plot(times, temperatures, marker='o', linestyle='-', color='b')

# Beschrifte die Achsen
plt.xlabel('Uhrzeit')
plt.ylabel('Temperatur (°C)')

# Titel hinzufügen
plt.title(f'Temperaturverlauf in {ort} im Laufe des Tages')

# Zeige das Diagramm an
plt.grid(True)
plt.show()
