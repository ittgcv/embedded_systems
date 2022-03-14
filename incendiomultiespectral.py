from gmplot import gmplot
#from GPSPhoto import gpsphoto
import csv
import math
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from skimage import data, io, filters,  color,  exposure,  img_as_float
import time
import numpy as np

numimage=1
#from skimage.util import compare_images

#image = data.coins()
# ... or any other NumPy array!
#edges = filters.sobel(image)
#io.imshow(edges)
def distanceCalculation(point1_lat, point1_long, point2_lat, point2_long, unit ):
    try:
        degrees = np.rad2deg(math.acos((math.sin(np.deg2rad(point1_lat))*math.sin(np.deg2rad(point2_lat))) + (math.cos(np.deg2rad(point1_lat))*math.cos(np.deg2rad(point2_lat))*math.cos(np.deg2rad(point1_long-point2_long)))))
    except:
        degrees=0
    if unit=='km':
        distance=degrees*111.13384
    elif unit=='metter':
        distance=degrees*111.13384*1000
    elif unit=='mi':
        distance=degrees*69.05482
    else:
        # en millas nauticas
        distance=degrees*59.97662
    print(point1_lat, point1_long, point2_lat, point2_long, degrees, distance)
    return math.ceil(distance)
def showImages(imgray):
    im_eq=exposure.equalize_hist(imgray)
    cm=plt.get_cmap('jet')
    comp_equalized = compare_images(img1, imrgb, method='checkerboard')
    colored_image=cm(im_eq)
    io.imshow(img1)
    io.show()
#time.sleep(5)
def showHistograma(imgray):
    image=img_as_float(imgray)
    hist, bin_centers=exposure.histogram(image)
    #print(hist, max(hist))
    return np.argmax(hist)

data_source='/home/madperez/Documentos/investigacion/images/incendios/recorridocosta0120/'

#fig = plt.figure(figsize=(8, 9))
#gs = GridSpec(3, 2)
#ax0 = fig.add_subplot(gs[0, 0])
#ax1 = fig.add_subplot(gs[0, 1])
#ax2 = fig.add_subplot(gs[1:, :])
#showHistograma(imgray)
#ax0.imshow(img1, cmap='gray')
#ax0.set_title('Original')
#ax1.imshow(imrgb, cmap='gray')
#ax1.set_title('Equalized')
#ax2.imshow(colored_image)
#ax2.set_title('Checkerboard comparison')
#   io.imsave(data_source+'framecolor'+str(numimage)+'.jpeg', color.rgba2rgb(colored_image))
#for a in (ax0, ax1, ax2):
 #   a.axis('off')
#plt.tight_layout()
#plt.plot()
#plt.show()
dictDataRisk={}
dictDataNonRisk={}
listLat=[]
listLon=[]
listMax=[]
listDistance=[]
listLatRisk=[]
listLonRisk=[]
listMaxRisk=[]
listLatNonRisk=[]
listLonNonRisk=[]
listMaxNonRisk=[]
with open('droidtrack_busCosta.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count==0:
            gmap = gmplot.GoogleMapPlotter(float(row[0]), float(row[1]), 13)

        # Marker
        if line_count<1000:
            img1=io.imread(data_source+'costa'+str(line_count)+'.jpg')
            imhsv=color.rgb2hsv(img1)
            indexMax=showHistograma(imhsv[:, :, 0])
            hidden_gem_lat, hidden_gem_lon = float(row[0]),float( row[1])
            if line_count==0:
                previousLat=hidden_gem_lat
                previousLon=hidden_gem_lon
                distancePoint=0
            else:
                distancePoint=distanceCalculation(previousLat, previousLon, hidden_gem_lat, hidden_gem_lon, 'metter')
                previousLat=hidden_gem_lat
                previousLon=hidden_gem_lon
            listLat.append(hidden_gem_lat)
            listLon.append(hidden_gem_lon)
            listMax.append(indexMax)
            listDistance.append(distancePoint)
            gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue', title=str(line_count))
            if indexMax<30:
                listLatRisk.append(hidden_gem_lat)
                listLonRisk.append(hidden_gem_lon)
                listMaxRisk.append(indexMax)
                #dict_dataRisk={"contador":line_count, "latitud":hidden_gem_lat, "longitud":hidden_gem_lon, "maxhist":indexMax}
            else:
                listLatNonRisk.append(hidden_gem_lat)
                listLonNonRisk.append(hidden_gem_lon)
                listMaxNonRisk.append(indexMax)
                #dict_dataNonRisk={"contador":line_count, "latitud":hidden_gem_lat, "longitud":hidden_gem_lon, "maxhist":indexMax}
            print(row[0], row[1], indexMax, distancePoint)
        line_count += 1
    print(line_count)
# Draw
csv_columns=['contador', 'latitud', 'longitud', 'maxhist']
csv_file = "dataclassified.csv"
csv_file_all='dataall.csv'
try:
    with open(csv_file, 'w') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerows(zip(listLatRisk, listLonRisk, listMaxRisk))
        writer.writerows(zip(listLatNonRisk, listLonNonRisk, listMaxNonRisk))
        #writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        #writer.writeheader()
except IOError:
    print("I/O error")
try:
    with open(csv_file_all, 'w') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerows(zip(listLat, listLon, listMax, listDistance))
except IOError:
    print("I/O error")
gmap.scatter(listLatRisk, listLonRisk, 'red', size=90,  marker=False)
gmap.scatter(listLatNonRisk, listLonNonRisk, 'blue', size=90,  marker=False)
gmap.draw("my_map.html")
