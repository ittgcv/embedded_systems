# manejo de fecha y hora con csv
from datetime import datetime 
import time
#import pandas as pd
usuario='jaime'
for i in range(10):
    fecha=datetime.now()
    print(fecha.strftime("%x,%X"))
#droidfile = '/sdcard/Documents/droidtrack_bus1.txt'
    droidfile='rancho.txt'
    fh = open(droidfile, 'a')
    res = fh.write(usuario+','+fecha.strftime("%x,%X") + '\n')
    res = fh.close()
    time.sleep(30)
