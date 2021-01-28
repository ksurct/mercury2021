import math
class Motor():
    def __init__(self):
        self.speed = 0
class Sensor( ):
    def __init__(self):
        self.speed = 0

class Point():
    def __init__(self, x, y):
        self.X = x
        self.Y = y

class RobotControl(object):
    def __init__(self):
        pass
    #A manual function for overriding the Model control
    def setMotorSpeed(self, motorIndex, speed):
        pass
    #Sets all the speeds of all the motors
    def setAllMotorSpeeds(self, motor0, motor1, motor2, motor3):
        pass

    #Gets the probable point
    def getProbablePoint(self):
        pass

    #Gets the probable theta
    def getProbableTheta(self):
        pass

    #Moves the robot forward a distance at a certain speed
    def move(self, meters, speed):
        pass

    #Rotates the robot by degrees at speed
    def rotate(self, degrees, speed):
        pass

    def getSensorData(self):
        pass