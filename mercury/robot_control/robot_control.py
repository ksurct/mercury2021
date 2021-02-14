import math

class Sensor():
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
    #A manual function to set the direction of the motor
    def setMotorDirection(self, motorIndex, direction):
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

    #Reads a command string and operates motors and servos from that
    def runCommand(self, string):
        #String Template: {LEFT SPEED},{LEFT DIR},{RIGHT SPEED},{RIGHT DIR},{ARM SERVO PWM},{CLAW SERVO PWM}
        #example: string = 100,-1, 49, 1,
        commands = string.strip().split(',')

        self.setMotorSpeed(0,int(commands[0].strip()))
        self.setMotorSpeed(1,int(commands[0].strip()))
        self.setMotorSpeed(2,int(commands[2].strip()))
        self.setMotorSpeed(3,int(commands[2].strip()))

        self.setMotorDirection(0,int(commands[1].strip()))
        self.setMotorDirection(1,int(commands[1].strip()))
        self.setMotorDirection(2,int(commands[3].strip()))
        self.setMotorDirection(3,int(commands[3].strip()))