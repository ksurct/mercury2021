#!/usr/bin/env python
import time
import serial
ser = serial.Serial(  
   port='/dev/ttyUSB0',
   baudrate = 9600,
   parity=serial.PARITY_ODD,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)
counter=0
while True:
    #ser.write(0b1010100)
    #time.sleep(0.020)
    print(ser.read())
    #ser.write(1)
    #time.sleep(0.1)
    print("Went Through {} time".format(counter))
    counter += 1

