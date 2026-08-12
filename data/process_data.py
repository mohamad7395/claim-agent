import csv

rows = []
with open("data/airports_raw.dat", encoding="utf-8") as f:
    for r in csv.reader(f):
        iata, lat, lon = r[4], r[6], r[7]
        if len(iata) == 3 and iata.isalpha():
            rows.append([iata.upper(), lat, lon])

with open("data/airports.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["iata", "lat", "lon"])
    w.writerows(rows)

print(len(rows), "airports")