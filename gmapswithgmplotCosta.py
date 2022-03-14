from gmplot import gmplot
from GPSPhoto import gpsphoto
import csv
with open('droidtrack_busCosta.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    dlat=[]
    dlon=[]
    for row in csv_reader:
        if line_count==0:
            gmap = gmplot.GoogleMapPlotter(float(row[0]), float(row[1]), 13)

        # Marker
        hidden_gem_lat, hidden_gem_lon = float(row[0]),float( row[1])
        dlat.append(hidden_gem_lat)
        dlon.append(hidden_gem_lon)
        # marker permite agregar uno por uno
        #gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue', title=str(line_count))
        print(row[0], row[1])
        line_count += 1
    print(line_count)
# scatter y circle requiere una lista
gmap.scatter(dlat, dlon, 'red', size=60,  marker=False)
#gmap.circle(dlat, dlon, color='red', radius=10)
# Get the data from image file and return a dictionary
data = gpsphoto.getGPSData('IMG_20190321_104019.jpg')

# Place map

# Polygon
#golden_gate_park_lats, golden_gate_park_lons = zip(*[
#    (37.771269, -122.511015),
#    (37.773495, -122.464830),
#    (37.774797, -122.454538),
#    (37.771988, -122.454018),
#    (37.773646, -122.440979),
#    (37.772742, -122.440797),
#    (37.771096, -122.453889),
#    (37.768669, -122.453518),
#    (37.766227, -122.460213),
#    (37.764028, -122.510347),
#    (37.771269, -122.511015)
#    ])
#gmap.plot(golden_gate_park_lats, golden_gate_park_lons, 'cornflowerblue', edge_width=10)

# Scatter points
#top_attraction_lats, top_attraction_lons = zip(*[
#    (37.769901, -122.498331),
#    (37.768645, -122.475328),
#    (37.771478, -122.468677),
#    (37.769867, -122.466102),
#    (37.767187, -122.467496),
#    (37.770104, -122.470436)
#    ])
#gmap.scatter(top_attraction_lats, top_attraction_lons, '#3B0B39', size=40, marker=False)


# Draw
#gmap.apikey('')
gmap.draw("my_map.html")
