#!/usr/bin/env python
from time import sleep
from smbus2 import SMBusWrapper
address = 0x04
 
# Give the I2C device time to settle
sleep(2)
 
def writeData(data):
    with SMBusWrapper(1) as bus:
        print(address)
        print(bus.write_byte_data(address, 0, data))    
    # Decreasing delay may create more transmission
    
while True:
    writeData(int(input("hello: ")))