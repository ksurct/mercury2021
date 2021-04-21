import serial
import json

class Serial(object):
    
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        self.ser.flush()
        self.sensorData = ""
        self.encoderData = ""
        self.magnetData = ""

    def receiveData(self):
        if self.ser.in_waiting > 0:
            line = json.loads(self.ser.readline().decode('utf-8').rstrip())
            self.encoderData = line['encoder']
            self.sensorData = line['distance']
            self.magnetData = line['magnet']
    def getSensor(self):
        return self.sensorData

    def getEncoder(self):
        return self.encoderData

    def getMagnet(self):
        return self.magnetData


# import serial


# if __name__ == '__main__':
#     ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
#     ser.flush()
    
#     while True:
#         if ser.in_waiting > 0:
#             line = ser.readline().decode('utf-8').rstrip()
#             print(line)