import csv

with open('space.csv', encoding="utf8") as f:
    reader = csv.DictReader(f,delimiter='*', quotechar='"')
    data = sorted(reader,key = lambda x: x['ShipName'])
id_project = input()
while (id_project != 'stop'):
    id_project = int(id_project)
    for el in data:
        if int(el['ShipName']) == id_project:
            surname,name,patronymic = el['direction'].split()
            print(f'Корабль <ShipName> был отправлен с планеты: <planet> и его направление движения было: <direction>')
            break
        else:
            print('error.. er.. ror..')
            id_project = input()