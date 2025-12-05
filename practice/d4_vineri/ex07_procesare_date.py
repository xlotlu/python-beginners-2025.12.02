# încărcăm datele de temperatură din sursa csv
# calculăm mediile orare
# și le scriem în alt fișier (csv? json?)



import csv 

# când lucrăm cu date financiare sau cu date științifice
# nu folosim float!
from decimal import Decimal

try:
    from ex06_aplicatie_scheduling import parse_timespec
except ImportError:
    from practice.d4_vineri.ex06_aplicatie_scheduling import parse_timespec


# 1. read the csv

#csv.reader(fp) # returnează liste
#csv.DictReader(fp) # returnează dicționare

def agg_temps(fname):
    with open(fname) as fp:
        reader = csv.reader(fp)

        hourly = []
        old_hour = None

        results = []

        for time, temp in reader:
            time = parse_timespec(time)
            #temp = Decimal(temp)
            temp = float(temp)

            if time.hour != old_hour and old_hour is not None:
                # s-a schimbat ora.
                # facem agregarea pe valorile acumulate.

                avg = sum(hourly) / len(hourly)
                # și construim rezultatele
                results.append((old_hour, avg))

                # și resetăm acumulatorul
                hourly = []

            hourly.append(temp)
            old_hour = time.hour
        
        # don't forget to handle the latest hour
        avg = sum(hourly) / len(hourly)
        results.append((old_hour, avg))

    return results

aggreggates = agg_temps("data/temperatures.csv")

# am uitat să punem encoding="utf-8",
# dar e în regulă, pt. că fișierul e doar cu numere și date
# (nu are nimic de encodat-decodat)

with open("aggreggates.csv", 'w') as fp:
    writer = csv.writer(fp)
    for row in aggreggates:
        writer.writerow(row)

    # sau 
    #writer.writerows(aggreggates)
