import gmaps
gmaps.configure(api_key='AIzaSyD9O9GJekIVGUU_-EDEykUo3xZBiXr7Sl0')
from GPSPhoto import gpsphoto
import anvil.server

anvil.server.connect("XSZ7HYCEBQPJDPXLRJEJUNC2-7KYZ3TJAUYOFBT3H")
@anvil.server.callable
def dataphoto():
    # Get the data from image file and return a dictionary
    data = gpsphoto.getGPSData('IMG_20190321_104019.jpg')
    rawData = gpsphoto.getRawData('IMG_20190321_104019.jpg')

    # Print out just GPS Data of interest
    print(data)
    print(data['Latitude'])
    for tag in data.keys():
        print("%s: %s" % (tag, data[tag]))

    # Print out raw GPS Data for debugging
    for tag in rawData.keys():
        print("%s: %s" % (tag, rawData[tag]))
    return data
#new_york_coordinates = (40.75, -74.00)
#gmaps.figure(center=new_york_coordinates, zoom_level=12)
#locations=[[data['Latitude'], data['Longitude']]]
#weights=[50]
#fig = gmaps.figure()
#fig.add_layer(gmaps.heatmap_layer(locations, weights=weights))
#fig
anvil.server.wait_forever()
