from gmplot import gmplot
import pandas as pd
data = pd.read_csv("tpr4.txt")
print(data.head())
# muestra los nombres de las columnas
print(data.columns)
# pone nombres a las columnas
data.columns=['trabajador', 'latitud','longitud','fecha', 'hora']
listLatRisk=[]
listLonRisk=[]
listLatNonRisk=[]
listLonNonRisk=[]
for i, rows in data.iterrows():
    if i==0:
        gmap = gmplot.GoogleMapPlotter(rows['latitud'], rows['longitud'], 13)
    listLatRisk.append(rows['latitud'])
    listLonRisk.append(rows['longitud'])
    print(i, rows['latitud'], rows['longitud'])
    #gmap.marker(rows['latitud'], rows['longitud'], 'cornflowerblue', title=str(rows['latitud'])+','+str(rows['longitud'])+','+str(float(rows['distancia'])/2))
    gmap.marker(rows['latitud'], rows['longitud'], 'cornflowerblue', title=str(rows['latitud'])+','+str(rows['longitud']))
gmap.scatter(listLatRisk, listLonRisk, 'red', size=90,  marker=False)
gmap.draw("my_map.html")
print(len(listLatRisk))
