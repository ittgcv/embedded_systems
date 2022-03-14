from gmplot import gmplot
import pandas as pd
data = pd.read_csv("dataall.csv") 
data.columns=['latitud', 'longitud', 'maximo', 'distancia']
print(data.head())
print(data.columns)
listLatRisk=[]
listLonRisk=[]
listLatNonRisk=[]
listLonNonRisk=[]
for i, rows in data.iterrows():
    if i==0:
        gmap = gmplot.GoogleMapPlotter(rows['latitud'], rows['longitud'], 13)
    if rows['maximo']<30.0 and rows['distancia']>30:
        listLatRisk.append(rows['latitud'])
        listLonRisk.append(rows['longitud'])
        print(i, rows['latitud'], rows['distancia'])
        gmap.marker(rows['latitud'], rows['longitud'], 'cornflowerblue', title=str(rows['latitud'])+','+str(rows['longitud'])+','+str(float(rows['distancia'])/2))
    else:
        listLatNonRisk.append(rows['latitud'])
        listLonNonRisk.append(rows['longitud'])
gmap.scatter(listLatRisk, listLonRisk, 'red', size=90,  marker=False)
gmap.scatter(listLatNonRisk, listLonNonRisk, 'blue', size=90,  marker=False)
gmap.draw("my_map.html")
print(len(listLatRisk))
