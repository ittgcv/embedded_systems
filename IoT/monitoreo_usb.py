import serial
import struct
import time
import readline
import anvil.server

anvil.server.connect("RG66VRAXBTO3ARVWG7KMRDQA-CPY4G7ZNUH2RZO53")

ser = serial.Serial('/dev/ttyACM0', baudrate = 115200, timeout = 3.0)
##arduino.open()

@anvil.server.callable
def Sensor():
    while True:
        if ser.in_waiting > 0:
            txt= ser.readline().decode('utf-8').rstrip()
##            time.sleep(.5)
            cadena = txt
            
            if cadena.find("1")>=0:
                estado = "Se activo el sensor #1"
                print ("se encenddio el sensor 1")
            else:
                if cadena.find("2")>=0:
                    estado="Se activo el sensor #2"
                    print ("se encenddio el sensor 2")
                else:
                    if cadena.find("3")>=0:
                        estado = "3"
                        print("se encendio el sensor 3")
                    else:
                        if cadena.find("4") >=0:
                            estado = "Se activo el sensor #4"
####                            print("se encendio el sensor 4")
            numero=estado
            return_value = anvil.server.call('Recibir', numero)
            
  
    
Sensor()

anvil.server.wait_forever()
