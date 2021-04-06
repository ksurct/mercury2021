import math
from mercury.settings.settings import settings
from mercury.common.point import Point
from time import sleep
from mercury.robot_control.robot_control import RobotControl
from mercury.motors.ServoModel import ServoModel
from mercury.sensors.sensors import Sensor
from mercury.communication.serial import Serial
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
        """self.sensorRB = Sensor("RB") #Right Back Sensor
        self.sensorRF = Sensor("RF") #Right Front Sensor
        self.sensorFR = Sensor("FR") #Front Right Sensor
        self.sensorFM = Sensor("FM") #Front Middle Sensor
        self.sensorFL = Sensor("FL") #Front Left Sensor
        self.sensorLF = Sensor("LF") #Left Front Sensor
        self.sensorLB = Sensor("LB") #Left Back Sensor"""
        self._sensors = [Sensor("RB"), Sensor("RF"), Sensor("FR"), Sensor("FM"), Sensor("FL"), Sensor("LF"), Sensor("LB")]
        self.serialData = Serial() 
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
        # ADD THIS: At this point set GPIO pin to high telling the arduino, the pi wants data.
        serialData.receiveData
        # ADD THIS: At this point, we have the data so set GPIO pin to low
        serialSensorData = serialData.getSensor()
        for i in range(0, _sensors.len()):
            _sensors[i].update(serialSensorData[i])
        return self._sensors

    #Sets the servo motor's angle to the given int degrees
    def setArmServo(self, degrees):
        self._armServo.updateAbsoluteAngle(degrees)
        pass
    def setClawServo(self, degrees):
        pass
        self._clawServo.updateAbsoluteAngle(degrees)

    
    def createCommandInstruction(self, key):
        #forward
        global speed
        if (key == "w"):
            if (speed > 0 and speed <= 100):
                return "CONTINUOUS, " + str(int(speed)) + ", " + str(int(speed)) + ", 90, 90"
                #return "DISCRETE, MOVE, 100, " + str(int(speed)) + ", 90, 90"
            else:
                return "CONTINUOUS, " + 100 + ", " + 100 + ", 90, 90"
                #return "DISCRETE, MOVE, 100, " + 100 + ", 90, 90"
        #left
        elif (key == "d"):
            if (speed > 0 and speed <= 100):
                return "CONTINUOUS, " + str(int(speed*-1)) + ", " + str(int(speed)) + ", 90, 90"
            else:
                return "CONTINUOUS, " + -100 + ", " + 100 + ", 90, 90"
        #right
        elif (key == "a"):
            if (speed > 0 and speed <= 100):
                return "CONTINUOUS, " + str(int(speed)) + ", " + str(int(-1*speed)) + ", 90, 90"
            else:
                return "CONTINUOUS, " + 100 + ", " + -100 + ", 90, 90"
        #stop
        elif(key == "s"):
            return "CONTINUOUS, 0, 0, 90, 90"
            #return "DISCRETE, ROTATE, 0, 0, 90, 90"
        elif(key == "m"):
            return "CONTINUOUS, 0, 0, 90, 90"
        #set speed (1-0, 0 being 10)
        elif (key == "1"):
            speed = 10
        elif (key == "2"):
            speed = 20
        elif (key == "3"):
            speed = 30
        elif (key == "4"):
            speed = 40
        elif (key == "5"):
            speed = 50
        elif (key == "6"):
            speed = 60
        elif (key == "7"):
            speed = 70
        elif (key == "8"):
            speed = 80
        elif (key == "9"):
            speed = 90
        elif (key == "0"):
            speed = 100
