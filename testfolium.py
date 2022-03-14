# herramienta para mostrar coordenadas geograficas
import folium
import pandas as pd
#Create base map
map = folium.Map(location=[16.75724,-93.17252], zoom_start = 8)
#Add Marker
#folium.Marker(location=[37.4074687,-122.086669], popup = "Google HQ", icon=folium.Icon(color = 'gray')).add_to(map)
#f = open('coordenadas.txt', 'r') 
#data = f.readlines()
# 
#for line in data:
#    words = line.split()
#    print words
data = pd.read_csv('coordenadas.txt', sep=",", header=None)
data.columns = ["longitude", "latitude", "fecha"]
print(data.head())
for index, row in data.iterrows():
    folium.Marker(location=[row["longitude"],row["latitude"]], popup = "bici", icon=folium.Icon(color = 'gray')).add_to(map)
#Save the map
map.save("map1.html")
