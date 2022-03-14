from bluetooth import *
devices = discover_devices()
for device in devices:
    print([_ for _ in find_service(address=device) if 'RFCOMM' in _['protocol'] ])
# now manually select the desired device or hardcode its name/mac whatever in the script
bt_addr = '20:34:FB:A6:DB:41'
port = [_ for _ in find_service(address=bt_addr) if 'RFCOMM' in _['protocol']][0]['port']
s = BluetoothSocket(RFCOMM)
s.connect((bt_addr, port))
while True :
   message = raw_input('Send:')
   if not message : 
       break
   s.send(message+'\n')
   data = s.recv(1024)
   print 'Received', `data`
s.close()
