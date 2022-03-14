import androidhelper,  time
#import cv
def distancia(pos_actual,pos_previo):
    cdis=((pos_actual["latitude"]-pos_previo["latitude"])**2+ (pos_actual["longitude"]-pos_previo["longitude"])**2)**.5
    #if cdis
    #droid.cameraCapturePicture('/sdcard/Documents/imagentest.jpg')
    return cdis
gpsfile='/sdcard/Documents/coordenadas.txt'
droid = androidhelper.Android()
droid.startLocating()
time.sleep(10)
counter=0
while counter<500:
    l=droid.readLocation()
    time.sleep(10)
    r=l.result
    print(r)
    
    try:
        r1=r["network"]
    except:
        try:
            r1=r["gps"]
        except:
            print("cadena no considerada",r)
    if counter>0:
        cdis=distancia(r1,previous_lecture)
        if cdis>0:
            #droid.cameraCapturePicture('/sdcard/Documents/combi'+str(counter)+'.jpg')
            outstr=str(r1["latitude"])+","+ str(r1["longitude"]) +","+time.strftime("%d/%m/%Y")+ ","+ str(cdis)
            fh=open(gpsfile,'a')
            res=fh.write(outstr+'\n')
            res=fh.close()
            print(r1["latitude"],r1["longitude"],cdis)
    previous_lecture=r1
    counter+=1
droid.stopLocating()