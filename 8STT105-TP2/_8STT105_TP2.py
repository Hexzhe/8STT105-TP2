import csv
import statistics
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Earthquake:
    date: datetime
    latitude: float
    longitudes: float
    depth: float
    magnitude: float
    magType: str
    place: str

print("8STT105 - TP2 - Partie 2")

earthquakes = []

with open('eqarchive-en.csv') as csvfile: #first load
    readCSV = csv.reader(csvfile, delimiter=',')
    first = True
    for row in readCSV:
        if first == True: #skip headers
            first = False
            continue

        earthquakes.append(Earthquake(datetime.strptime(row[0], "%Y-%m-%dT%H:%M:%S%z"), float(row[1]), float(row[2]), float(row[3]), float(row[4]), row[5], row[6]))

print(f"Tremblements de terre chargés: {len(earthquakes)}")

#TODO: Quelle est la probabilité d'avoir un tremblement de terre de magnitude 5 ou plus?

#TODO: L'impact monétaire d'un tremblement de terre est fonction de sa magnétude
#          0$ s'il est de moins de 1
#          5k$ s'il est de 1 à moins de 2
#          25k$ s'il est de 2 à moins de 3
#          125k$ s'il est de 3 à moins de 4
#          500k$ s'il est de 4 à moins de 5
#          2000k$ s'il est de 5 à moins de 6
#          10000k$ s'il est de 6 ou plus
#      Quelle est l'espérance du coût des tremblements de terre au Canada sur 10 ans?

#TODO: RAPPORT: Dans votre rapport, vous devez caractériser la population, l'échantillon, la v.a., la loi de probabilité, et justifiez vos réponses.