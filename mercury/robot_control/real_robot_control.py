import math
from mercury.settings.settings import settings
from mercury.common.point import Point
from time import sleep
from mercury.robot_control.robot_control import RobotControl
from mercury.motors.ServoModel import ServoModel
from mercury.sensors.sensors import Sensor
from mercury.communication.serial import Serial

#-----------------------------
import RPi.GPIO as GPIO
#-----------------------------

# Simple setup to allow for playground usage of the real robot
if (settings['instance'].value == 'realbot'):
    from mercury.motors.motor import Motor
else:
    from mercury.motors.dummy_motors import Motor

class RealRobotControl(RobotControl):
    def __init__(self):
        self.NUM_MOTORS = 4
        self._motors = Motor.getDefaultMotors()
        self._probablePoint = Point(0, 0)
        self._probableTheta = 0

        #Creates a Serial Object to read data
        self.serialData = Serial()
        #Sensors
        """self.sensorRB = Sensor("RB") #Right Back Sensor
        self.sensorRF = Sensor("RF") #Right Front Sensor
        self.sensorFR = Sensor("FR") #Front Right Sensor
        self.sensorFM = Sensor("FM") #Front Middle Sensor
        self.sensorFL = Sensor("FL") #Front Left Sensor
        self.sensorLF = Sensor("LF") #Left Front Sensor
        self.sensorLB = Sensor("LB") #Left Back Sensor"""
        self._sensors = [Sensor("RB"), Sensor("RF"), Sensor("FR"), Sensor("FM"), Sensor("FL"), Sensor("LF"), Sensor("LB")]

        #Stores Magnet Data read from arduino (float)
        self.magnetData = 0.0

        #Stores encoder data read from arduino (three floats)
        self.encoderData = [0.0, 0.0, 0.0, 0.0]

        # Created A servo motor from the ServoModel Class.
        self._armServo = ServoModel('Arm',1,0,250)
        self._clawServo = ServoModel('Claw',0,0,250)
        
        #TODO: This is a total guess
        self.MAX_MPS = 1

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
    def setMotorSpeedByIndex(self, motorIndex, speed):
        self._motors[motorIndex].setSpeed(speed)

        # We can no longer predict our location
        self._probableTheta = 0
        self._probablePoint = Point(0,0)
        self.resetLocation()

    #A manual function for overriding the Model control
    def setMotorSpeedByName(self, motorName, speed):
        for m in self._motors:
            if (m.name == motorName):
                m.setSpeed(speed)
        self.resetLocation()

    # Called when we can no longer predict where we are.
    def resetLocation(self):
        self._probableTheta = 0
        self._probablePoint = Point(0,0)

    #Sets all the speeds of all the motors
    def setAllMotorSpeeds2(self, motor0, motor1, motor2, motor3):
        self._motors[0].setSpeed(motor0)
        self._motors[1].setSpeed(motor1)
        self._motors[2].setSpeed(motor2)
        self._motors[3].setSpeed(motor3)
        self.resetLocation()

    #Sets all the speeds of all the motors
    def setAllMotorSpeeds(self, speed):
        print(self._motors[0].__class__)
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
        print("Made it")
        # TODO: Figure out time constraints needed for this to work
        speed = self.metersPerSecondToPercent(speedMpS)
        self._probableTheta += degrees
        if (degrees < 0):
            speed = -speed
        self.setAllMotorSpeeds2(speed, speed, -speed, -speed)
        sleep(3)
        self.setAllMotorSpeeds2(0,0,0,0)

    def getSensorData(self):
        # Gets Sensor Data from Arduino (ints)
        #Setting up GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        #Currently set up as pin 18
        GPIO.setup(18,GPIO.OUT)

        GPIO.output(18,GPIO.HIGH)
        self.serialData.receiveData
        GPIO.output(18,GPIO.LOW)
        self.serialData.receiveData

        serialSensorData = self.serialData.getSensor()
        for i in range(0, len(self._sensors)):
            self._sensors[i].update(serialSensorData[i])
            print (serialSensorData[i]) 
        return self._sensors

    def getMagnetData(self):
        # Gets Magnet Data from Arduino (float)
        #Setting up GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        #Currently set up as pin 18
        GPIO.setup(18,GPIO.OUT)

        GPIO.output(18,GPIO.HIGH)
        self.serialData.receiveData
        GPIO.output(18,GPIO.LOW)

        serialMagnetData = self.serialData.getMagnet()
        self.magnetData = serialMagnetData
        print (magnetData)
        return self.magnetData

    def getEncoderData(self):
        # Gets Encoder Data from Arduino
        #Setting up GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        #Currently set up as pin 18
        GPIO.setup(18,GPIO.OUT)

        GPIO.output(18,GPIO.HIGH)
        self.serialData.receiveData
        GPIO.output(18,GPIO.LOW)

        serialEncoderData = self.serialData.getEncoder()
        for i in range(0, len(self.encoderData)):
            self.encoderData[i] = serialEncoderData[i]
            print (serialEncoderData[i])
        return self.encoderData

    #Sets the servo motor's angle to the given int degrees
    def setArmServo(self, degrees):
        self._armServo.updateAbsoluteAngle(degrees)
        pass
    def setClawServo(self, degrees):
        pass
        self._clawServo.updateAbsoluteAngle(degrees)
