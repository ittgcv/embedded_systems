import folium
from GPSPhoto import gpsphoto
from os import listdir
from os.path import isfile, join
mypath='/home/madperez/Documentos/investigacion/images/pastura'
onlyfiles = [f for f in listdir(mypath) if isfile(join('/home/madperez/Documentos/investigacion/images/pastura', f))]
# Get the data from image file and return a dictionary
for i in onlyfiles:
    data = gpsphoto.getGPSData('/home/madperez/Documentos/investigacion/images/pastura/'+i)
    print(data)
    rawData = gpsphoto.getRawData(mypath+i)
    map = folium.Map(location=[data['Latitude'],data['Longitude']], zoom_start = 8)
    folium.Marker(location=[data["Latitude"],data["Longitude"]], popup = "sheep", icon=folium.Icon(color = 'gray')).add_to(map)

# Print out just GPS Data of interest
for tag in data.keys():
    print "%s: %s" % (tag, data[tag])

# Print out raw GPS Data for debugging
#for tag in rawData.keys():
#    print "%s: %s" % (tag, rawData[tag])
map.save("map1.html")
#AIzaSyD9O9GJekIVGUU_-EDEykUo3xZBiXr7Sl0
