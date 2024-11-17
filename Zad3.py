streets = ['Jagodowa','Lipowa','Kwiatowa','Kasztanowa','Palna']
blocks = [1,2,3,4,5]
flats =['/1','/2','/3','/3','/4','/5','/6','/7','/8','/9','/10']

for street in streets:
    for block in blocks:
        for flat in flats:
            print (f"{street} {block} , {flat}")