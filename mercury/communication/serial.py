import serial
import json

class Serial(object):
    
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        self.ser.flush()
        self.sensorData = ""
        self.encoderData = ""
        self.magnetData = ""

    def receiveData(self):
        while (not self.ser.in_waiting > 0):
            if self.ser.in_waiting > 0:
                line = self.ser.readline().decode('utf-8').rstrip()
                jsonLine = json.loads(line)
                self.encoderData = jsonLine['encoder']
                self.sensorData = jsonLine['distance']
                self.magnetData = jsonLine['magnet']
    
    def getSensor(self):
        return self.sensorData

    def getEncoder(self):
        return self.encoderData

    def getMagnet(self):
        return self.magnetData


