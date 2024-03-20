import csv

with open('space.csv', encoding='utf8') as f:
    reader = csv.reader(f, delimiter='*', quotechar='"')
    answer = list(reader)[1:]
    for ShipName, planet, coord_place, direction in answer:
        print(answer)
with open('space_new.tx','w',newline='', encoding='utf-8') as fi:
    w = csv.writer(fi)
    w.writerow(['ShipName','planet','coord_place','direction'])
    w.writerows(answer)