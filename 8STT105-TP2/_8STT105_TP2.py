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

#Quelle est la probabilité d'avoir un tremblement de terre de magnitude 5 ou plus?
countGrtrOrEqu5 = sum((earthquake.magnitude >= 5) for earthquake in earthquakes)

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

countAll = countLess1 + countBtwn1And2 + countBtwn2And3 + countBtwn3And4 + countBtwn4And5 + countBtwn5And6 + countGrtrOrEqu6

costLess1 = countLess1*0
costBtwn1And2 = countBtwn1And2*5000
costBtwn2And3 = countBtwn2And3*25000
costBtwn3And4 = countBtwn3And4*125000
costBtwn4And5 = countBtwn4And5*500000
costBtwn5And6 = countBtwn5And6*2000000
costGrtrOrEqu6 = countGrtrOrEqu6*10000000

costAll = costLess1 + costBtwn1And2 + costBtwn2And3 + costBtwn3And4 + costBtwn4And5 + costBtwn5And6 + costGrtrOrEqu6

print(f"Nombre total: {countAll:0,.0f}")
print(f"Coût total  : {costAll:0,.2f}$")
print(f"Nombre de magnitude >= 5: {countGrtrOrEqu5} ({round(100*countGrtrOrEqu5/len(earthquakes), 2)}%)\n")

print("Coût total (par magnitude):")
print(f"    <1  | {countLess1:>6,.0f} x 0$      | {costLess1:16,.2f}$")
print(f"    1-2 | {countBtwn1And2:>6,.0f} x 5k$     | {costBtwn1And2:16,.2f}$")
print(f"    2-3 | {countBtwn2And3:>6,.0f} x 25k$    | {costBtwn2And3:16,.2f}$")
print(f"    3-4 | {countBtwn3And4:>6,.0f} x 125k$   | {costBtwn3And4:16,.2f}$")
print(f"    4-5 | {countBtwn4And5:>6,.0f} x 500k$   | {costBtwn4And5:16,.2f}$")
print(f"    5-6 | {countBtwn5And6:>6,.0f} x 2000k$  | {costBtwn5And6:16,.2f}$")
print(f"    >6  | {countGrtrOrEqu6:>6,.0f} x 10000k$ | {costGrtrOrEqu6:16,.2f}$")
print("------------------------------------------------")
print(f"          {countAll:<16,.0f}   {costAll:16,.2f}$\n")

#Quelle est l'espérance du coût des tremblements de terre au Canada sur 10 ans?
countsPerYear = []
currentCountPerYear = 0
currentYear = None
i = 0
while i < len(earthquakes): #count per year
    if currentYear != earthquakes[i].date.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0):
        if currentYear != None:
            countsPerYear.append(currentCountPerYear)
        currentYear = earthquakes[i].date.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
        currentCountPerYear = 0
    currentCountPerYear += 1
    i += 1

yearCount = len(countsPerYear)

avgCountLess1 = round(countLess1/yearCount)
avgCountBtwn1And2 = round(countBtwn1And2/yearCount)
avgCountBtwn2And3 = round(countBtwn2And3/yearCount)
avgCountBtwn3And4 = round(countBtwn3And4/yearCount)
avgCountBtwn4And5 = round(countBtwn4And5/yearCount)
avgCountBtwn5And6 = round(countBtwn5And6/yearCount)
avgCountGrtrOrEqu6 = round(countGrtrOrEqu6/yearCount)

#à partir d'ici on prévilégie la constance du rapport vs l'exactitude des nombres en réutilisant les moyennes precedentes pour effectuer nos calculs
avgCountAll = avgCountLess1 + avgCountBtwn1And2 + avgCountBtwn2And3 + avgCountBtwn3And4 + avgCountBtwn4And5 + avgCountBtwn5And6 + avgCountGrtrOrEqu6

avgCostLess1 = avgCountLess1*0
avgCostBtwn1And2 = avgCountBtwn1And2*5000
avgCostBtwn2And3 = avgCountBtwn2And3*25000
avgCostBtwn3And4 = avgCountBtwn3And4*125000
avgCostBtwn4And5 = avgCountBtwn4And5*500000
avgCostBtwn5And6 = avgCountBtwn5And6*2000000
avgCostGrtrOrEqu6 = avgCountGrtrOrEqu6*10000000

avgCostAll = avgCostLess1 + avgCostBtwn1And2 + avgCostBtwn2And3 + avgCostBtwn3And4 + avgCostBtwn4And5 + avgCostBtwn5And6 + avgCostGrtrOrEqu6

print(f"Nombre d'années distinctes: {yearCount}")
print(f"Nombre moyen par année:     {avgCountAll:0,.0f}")
print(f"Coût moyen par année:       {avgCostAll:0,.2f}$")
print(f"Coût moyen sur 10 ans:      {avgCostAll*10:0,.2f}$\n")

print("Coût moyen (par magnitude, par année, arrondi):")
print(f"    <1  | {avgCountLess1:>5,.0f} x 0$      | {avgCostLess1:13,.2f}$")
print(f"    1-2 | {avgCountBtwn1And2:>5,.0f} x 5k$     | {avgCostBtwn1And2:13,.2f}$")
print(f"    2-3 | {avgCountBtwn2And3:>5,.0f} x 25k$    | {avgCostBtwn2And3:13,.2f}$")
print(f"    3-4 | {avgCountBtwn3And4:>5,.0f} x 125k$   | {avgCostBtwn3And4:13,.2f}$")
print(f"    4-5 | {avgCountBtwn4And5:>5,.0f} x 500k$   | {avgCostBtwn4And5:13,.2f}$")
print(f"    5-6 | {avgCountBtwn5And6:>5,.0f} x 2000k$  | {avgCostBtwn5And6:13,.2f}$")
print(f"    >6  | {avgCountGrtrOrEqu6:>5,.0f} x 10000k$ | {avgCostGrtrOrEqu6:13,.2f}$")
print("--------------------------------------------")
print(f"          {avgCountAll:<15,.0f}   {avgCostAll:13,.2f}$\n")