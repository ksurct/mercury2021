import math

#TODO: Remove and utilize normal motor module
class Motor():
    def __init__(self):
        self.speed = 0

#TODO: remove and add to proper module.
class Sensor( ):
    def __init__(self):
        self.speed = 0

#TODO: Remove and add to common
class Point():
    def __init__(self, x, y):
        self.X = x
        self.Y = y

class RealRobotControl(object):
    def __init__(self):
        self._motors = [Motor(), Motor(), Motor(), Motor()]
        self._probablePoint = Point(0, 0)
        self._probableTheta = 0
        self._sensors = [Sensor(), Sensor(), Sensor(), Sensor(), Sensor()] 

    #A manual function for overriding the Model control
    def setMotorSpeed(self, motorIndex, speed):
        self._motors[motorIndex].speed = speed
        self._probableTheta = 0
        self._probablePoint = Point(0,0)
    
    #Sets all the speeds of all the motors
    def setAllMotorSpeeds(self, motor0, motor1, motor2, motor3):
        self._motors[0].speed = motor0
        self._motors[1].speed = motor1
        self._motors[2].speed = motor2
        self._motors[3].speed = motor3

    #Gets the probable point
    def getProbablePoint(self):
        return self._probablePoint

    #Gets the probable theta
    def getProbableTheta(self):
        return self._probableTheta

    #Moves the robot forward a distance at a certain speed
    def move(self, meters, speed):
        # TODO: need to run for only meters / speed time
        self._probablePoint.X += math.cos(self._probableTheta) * meters
        self._probablePoint.Y += math.sin(self._probableTheta) * meters
        for i in range(0, 4):
            self._motors[i].speed = speed
        
    #Rotates the robot by degrees at speed
    def rotate(self, degrees, speed):
        # TODO: Figure out time constraints needed for this to work
        self._probableTheta += degrees
        if (degrees < 0):
            speed = -speed
        self.setAllMotorSpeeds(speed, speed, -speed, -speed)

    def getSensorData(self):
        return self._sensors