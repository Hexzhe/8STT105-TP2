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

print("8STT105 - TP2 - Partie 2\n")

earthquakes = []

with open('eqarchive-en.csv') as csvfile: #first load
    readCSV = csv.reader(csvfile, delimiter=',')
    first = True
    for row in readCSV:
        if first == True: #skip headers
            first = False
            continue

        earthquakes.append(Earthquake(datetime.strptime(row[0], "%Y-%m-%dT%H:%M:%S%z"), float(row[1]), float(row[2]), float(row[3]), float(row[4]), row[5], row[6]))

print(f"Tremblements de terre chargés: {len(earthquakes):0,.0f}\n")

#Quelle est la probabilité d'avoir un tremblement de terre de magnitude 5 ou plus?
countGrtrOrEqu5 = sum((earthquake.magnitude >= 5) for earthquake in earthquakes)
print(f"Nombre de magni. >= 5: {countGrtrOrEqu5} ({round(100*countGrtrOrEqu5/len(earthquakes), 2)}%)\n")

#L'impact monétaire d'un tremblement de terre est fonction de sa magnétude
#          0$ s'il est de moins de 1
#          5k$ s'il est de 1 à moins de 2
#          25k$ s'il est de 2 à moins de 3
#          125k$ s'il est de 3 à moins de 4
#          500k$ s'il est de 4 à moins de 5
#          2000k$ s'il est de 5 à moins de 6
#          10000k$ s'il est de 6 ou plus

countLess1 = sum((earthquake.magnitude < 1) for earthquake in earthquakes)
countBtwn1And2 = sum((earthquake.magnitude >= 1 and earthquake.magnitude < 2) for earthquake in earthquakes)
countBtwn2And3 = sum((earthquake.magnitude >= 2 and earthquake.magnitude < 3) for earthquake in earthquakes)
countBtwn3And4 = sum((earthquake.magnitude >= 3 and earthquake.magnitude < 4) for earthquake in earthquakes)
countBtwn4And5 = sum((earthquake.magnitude >= 4 and earthquake.magnitude < 5) for earthquake in earthquakes)
countBtwn5And6 = sum((earthquake.magnitude >= 5 and earthquake.magnitude < 6) for earthquake in earthquakes)
countGrtrOrEqu6 = sum((earthquake.magnitude >= 6) for earthquake in earthquakes)

print("Impact monétaire total (par magnitude):")
print(f"    <1  : {countLess1:>6,.0f} x 0$      : {countLess1*0:16,.2f}$")
print(f"    1-2 : {countBtwn1And2:>6,.0f} x 5k$     : {countBtwn1And2*5000:16,.2f}$")
print(f"    2-3 : {countBtwn2And3:>6,.0f} x 25k$    : {countBtwn2And3*25000:16,.2f}$")
print(f"    3-4 : {countBtwn3And4:>6,.0f} x 125k$   : {countBtwn3And4*125000:16,.2f}$")
print(f"    4-5 : {countBtwn4And5:>6,.0f} x 500k$   : {countBtwn4And5*500000:16,.2f}$")
print(f"    5-6 : {countBtwn5And6:>6,.0f} x 2000k$  : {countBtwn5And6*2000000:16,.2f}$")
print(f"    >6  : {countGrtrOrEqu6:>6,.0f} x 10000k$ : {countGrtrOrEqu6*10000000:16,.2f}$\n")

#Quelle est l'espérance du coût des tremblements de terre au Canada sur 10 ans?
costsPerYear = []
currentCostPerYear = 0
countsPerYear = []
currentCountPerYear = 0
currentYear = None
i = 0
while i < len(earthquakes): #count cost per year
    if currentYear != earthquakes[i].date.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0):
        if currentYear != None:
            costsPerYear.append(currentCostPerYear)
            countsPerYear.append(currentCountPerYear)
        currentYear = earthquakes[i].date.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
        currentCostPerYear = 0
        currentCountPerYear = 0

    if earthquakes[i].magnitude < 1:
        currentCostPerYear += 0
    elif earthquakes[i].magnitude >= 1 and earthquakes[i].magnitude < 2:
        currentCostPerYear += 5000
    elif earthquakes[i].magnitude >= 2 and earthquakes[i].magnitude < 3:
        currentCostPerYear += 25000
    elif earthquakes[i].magnitude >= 3 and earthquakes[i].magnitude < 4:
        currentCostPerYear += 125000
    elif earthquakes[i].magnitude >= 4 and earthquakes[i].magnitude < 5:
        currentCostPerYear += 500000
    elif earthquakes[i].magnitude >= 5 and earthquakes[i].magnitude < 6:
        currentCostPerYear += 2000000
    else:
        currentCostPerYear += 10000000

    currentCountPerYear += 1
    i += 1

print(f"Distinct years count:   {len(costsPerYear)}")
print(f"Average count per year: {statistics.mean(countsPerYear):0,.0f}")
print(f"Average cost per year:  {statistics.mean(costsPerYear):0,.2f}$")
print(f"10 years average:       {statistics.mean(costsPerYear)*10:0,.2f}$\n")