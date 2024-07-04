import datetime
import matplotlib.pyplot as plt
from metno_locationforecast import Place, Forecast

ort = Place("Madrid", 52.0302, 8.5325)
forecast = Forecast(ort, "daniel_vhs_bielefeld")
forecast.update()

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
plt.title('Temperaturverlauf im Laufe des Tages')

# Zeige das Diagramm an
plt.grid(True)
plt.show()
