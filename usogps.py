# -*-coding:utf8;-*-
# qpy:2
# qpy:console
# analiza imágenes aéreas, las clasifica como peligrosas o no en función de la cantidad de material combustible
# Basado en el histograma de la componene hue, se clasifica como peligrosa aquella que su máximo sea menor que 30
print "This is console module"

import androidhelper, time
import csv

droid = androidhelper.Android()
droid.startLocating()
time.sleep(10)
c = 0
lectura={}
while c < 5:

    l = droid.readLocation()
    R = l.result
    try:
        R = R["gps"]
        Lat = R["latitude"]
        Lon = R["longitude"]
        # R1 =R["network"]
        # Lat1=R1["latitude"]
        # Lon1=R1["longitude"]
        outstr = str(Lat) + "," + str(Lon)
        droidfile = '/sdcard/Documents/droidtrack_bus1.txt'
        print outstr  # , str(Lat1) , str(Lon1)
        fh = open(droidfile, 'a')
        res = fh.write(outstr + '\n')
        res = fh.close()
        time.sleep(30)
        c += 1
        print c
        date=time.strftime("%d/%m/%Y")
        print date
        lectura[c]=[outstr,date]
    except:
        time.sleep(10)
        print c
        print R
        c += 1
with open('/sdcard/Documents/datosgps.csv','wb') as csvfile:
    writer=csv.writer(csvfile)
    for key,value in lectura.items():
        writer.writerow([key,value])
