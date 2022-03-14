import gmaps
gmaps.configure(api_key='AIzaSyD9O9GJekIVGUU_-EDEykUo3xZBiXr7Sl0')
from GPSPhoto import gpsphoto
# Get the data from image file and return a dictionary
data = gpsphoto.getGPSData('IMG_20190321_104019.jpg')
rawData = gpsphoto.getRawData('IMG_20190321_104019.jpg')

# Print out just GPS Data of interest
print(data)
for tag in data.keys():
    print "%s: %s" % (tag, data[tag])

# Print out raw GPS Data for debugging
for tag in rawData.keys():
    print "%s: %s" % (tag, rawData[tag])
new_york_coordinates = (40.75, -74.00)
gmaps.figure(center=new_york_coordinates, zoom_level=12)
locations=[[data['Latitude'], data['Longitude']]]
weights=[50]
fig = gmaps.figure()
fig.add_layer(gmaps.heatmap_layer(locations, weights=weights))
fig
