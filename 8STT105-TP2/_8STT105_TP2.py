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

