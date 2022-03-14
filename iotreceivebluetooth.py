# echoclient.py

#import sys
from bluetooth import *
mydevices={'Redmi':'20:34:FB:A6:DB:41'}
#HOST = sys.argv[1]       # The remote host
PORT = 1                 # Server port
#HOST="24:0A:C4:AE:9D:EA"
HOST=mydevices['Redmi']
print(HOST)
s=BluetoothSocket( RFCOMM )

s.connect((HOST, PORT))

while True :
   message = raw_input('Send:')
   if not message : break
   s.send(message)
   data = s.recv(1024)
   print 'Received', `data`
s.close()
