import re

regex = r"^a.*\.html$"
dateinamen = ["ba12.html", "a45.html", "a45.HTML", "alles.html"]
for datei in dateinamen:
    if re.search(regex, datei) is not None:
        print(datei)
