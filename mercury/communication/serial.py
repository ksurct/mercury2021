import serial
import json

class Serial(object):
    
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        ser.flush()
        self.sensorData = ""
        self.encoderData = ""
        self.magnetData = ""

    def receiveData(self):
        while !(ser.in_waiting > 0):
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                jsonLine = json.loads(line)
                encoderData = jsonLine['encoder']
                sensorData = jsonLine['distance']
                magnetData = jsonLine['magnet']
    
    def getSensor(self):
        return sensorData

    def getEncoder(self):
        return encoderData

    def getMagnet(self):
        return magnetData


