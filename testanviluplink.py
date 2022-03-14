import anvil.server
import numpy as np
import math

anvil.server.connect("Y5ZZ5PNUIPHCKBRCYMX3EGDF-ZOKSV5KK2L7O5NHT")
@anvil.server.callable
def distanceCalculation(point1_lat, point1_long, point2_lat, point2_long, unit ):
    print('hola')
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

@anvil.server.callable
def distanceEfficient(listLat, listLon, unit ):
    flag=0
    distance=0
    for iLat, iLon in zip(listLat, listLon):
        print(iLat, iLon)
        if flag==0:
            point1_lat=float(iLat)
            point1_long=float(iLon)
            flag=1
        else:
            point2_lat=float(iLat)
            point2_long=float(iLon)
            try:
                degrees = np.rad2deg(math.acos((math.sin(np.deg2rad(point1_lat))*math.sin(np.deg2rad(point2_lat))) + (math.cos(np.deg2rad(point1_lat))*math.cos(np.deg2rad(point2_lat))*math.cos(np.deg2rad(point1_long-point2_long)))))
            except:
                degrees=0
            if unit=='km':
                distance+=degrees*111.13384
            elif unit=='metter':
                distance+=degrees*111.13384*1000
            elif unit=='mi':
                distance+=degrees*69.05482
            else:
                # en millas nauticas
                distance+=degrees*59.97662
            print(point1_lat, point1_long, point2_lat, point2_long, degrees, distance)
        point1_lat=float(iLat)
        point1_long=float(iLon)
    return math.ceil(distance)

@anvil.server.callable
def distanciaUnidades(dictUnidades):
    # calcula la distancia de la posicion del usuario a cada unidad
    # usa la unidad 1 como referencia
    unit='km'
    distance=0
    datosRef=dictUnidades['get_positiona']
    point1_lat=datosRef['latitud']
    point1_long=datosRef['longitud']
    distancias={}
    for key, value in dictUnidades.items():
        point2_lat=value['latitud']
        point2_long=value['longitud']
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
        distancias[key]=distance
    return distancias

anvil.server.wait_forever()
