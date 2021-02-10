import math
from mercury.settings.settings import settings
from mercury.common.point import Point
from time import sleep

# Simple setup to allow for playground usage of the real robot
if (settings['instance'].value == 'realbot'):
    from mercury.motors.motor import Motor
else:
    from mercury.motors.dummy_motors import Motor

#TODO: remove and add to proper module.
class Sensor( ):
    def __init__(self):
        self.speed = 0


class RealRobotControl(object):
    def __init__(self):
        self.NUM_MOTORS = 4
        self._motors = Motor.getDefaultMotors()
        self._probablePoint = Point(0, 0)
        self._probableTheta = 0
        self._sensors = [Sensor(), Sensor(), Sensor(), Sensor(), Sensor()] 
        
        #TODO: This is a total guess
        self.MAX_MPS = 0.5

    # This function converts a meters per second number into a 
    # Speed percent we can hand to the motors
    #
    # TODO: We may also need to do a line regression fit
    # to make a function that more accruatly handles 
    # the motor progression. That is if the percent to speed
    # function is non-linear.
    def metersPerSecondToPercent(self, mps):
        return mps / self.MAX_MPS 

    #A manual function for overriding the Model control
    def setMotorSpeed(self, motorIndex, speed):
        self._motors[motorIndex].setSpeed(speed)

        # We can no longer predict our location
        self._probableTheta = 0
        self._probablePoint = Point(0,0)
        self.resetLocation()

    #A manual function for overriding the Model control
    def setMotorSpeed(self, motorName, speed):
        for m in self._motors:
            if (m.name == motorName):
                m.setSpeed(speed)
        self.resetLocation()

    # Called when we can no longer predict where we are.
    def resetLocation(self):
        self._probableTheta = 0
        self._probablePoint = Point(0,0)

    #Sets all the speeds of all the motors
    def setAllMotorSpeeds(self, motor0, motor1, motor2, motor3):
        self._motors[0].setSpeed(motor0)
        self._motors[1].setSpeed(motor1)
        self._motors[2].setSpeed(motor2)
        self._motors[3].setSpeed(motor3)
        self.resetLocation()

    #Sets all the speeds of all the motors
    def setAllMotorSpeeds(self, speed):
        self._motors[0].setSpeed(speed)
        self._motors[1].setSpeed(speed)
        self._motors[2].setSpeed(speed)
        self._motors[3].setSpeed(speed)
        self.resetLocation()

    #Gets the probable point
    def getProbablePoint(self):
        return self._probablePoint

    #Gets the probable theta
    def getProbableTheta(self):
        return self._probableTheta

    #Moves the robot forward a distance at a certain speed
    # TODO: Current a blocking function. Remake so that we can
    # asynchronously handle moves.
    def move(self, meters, speedMpS):
        speed = self.metersPerSecondToPercent(speedMpS)
        self._probablePoint.x += math.cos(self._probableTheta) * meters
        self._probablePoint.y += math.sin(self._probableTheta) * meters
        for i in range(0, self.NUM_MOTORS):
            self._motors[i].setSpeed(speed)
        sleep(meters / speed)
        for i in range(0, self.NUM_MOTORS):
            self._motors[i].setSpeed(0)
        
    # Rotates the robot by degrees at speed
    def rotate(self, degrees, speedMpS):
        # TODO: Figure out time constraints needed for this to work
        speed = self.metersPerSecondToPercent(speedMpS)
        self._probableTheta += degrees
        if (degrees < 0):
            speed = -speed
        self.setAllMotorSpeeds(speed, speed, -speed, -speed)

    def getSensorData(self):
        return self._sensors