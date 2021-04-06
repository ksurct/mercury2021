import math

class RobotControl(object):
    def __init__(self):
        pass
    #A manual function for overriding the Model control
    def setMotorSpeedByIndex(self, motorIndex, speed):
        pass

    #Sets the motor with the given name to a speed
    def setMotorSpeedByName(self, motorName, speed):
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
    
    def setArmServo(self, degrees):
        pass

    def setClawServo(self, degrees):
        pass

    def createCommandInstruction(self, key):
        pass
    
    #Reads a command string and operates motors and servos from that
    def runCommand(self, string):
        #String Template: "CONTINUOUS",{LEFT SPEED},{RIGHT SPEED},{ARM SERVO DEGREES},{CLAW SERVO DEGREES}
        #example: string = CONTINUOUS,  100, 49, 180, 90

        #String Template: "DISCRETE", {"MOVE"/"ROTATE"}, {METERS/DEGREES}, {SPEED}, {CLAW SERVO DEGREES}, {ARM SERVO DEGREES}
        #example: string = DISCRETE, MOVE, 0.5, 50, 120, 180
        #example: string = DISCRETE, ROTATE, 90, 50, 145, 35\
        print("COMMAND STRING INPUT: ", string)
        commands = string.strip().split(',')

        if commands[0].strip() == 'CONTINUOUS':
            #ServoMotors:
            self.setArmServo(int(commands[3]))
            self.setClawServo(int(commands[4]))
            #DriveMotors:
            self.setMotorSpeedByIndex(0,int(commands[1].strip()))
            self.setMotorSpeedByIndex(1,int(commands[1].strip()))
            self.setMotorSpeedByIndex(2,int(commands[2].strip()))
            self.setMotorSpeedByIndex(3,int(commands[2].strip()))
        
        elif commands[0].strip() == 'DISCRETE':
            if commands[1].strip() == 'MOVE':
                self.move(float(commands[2]),float(commands[3]))
                #self.setClawAngle(int(commands[4]))
                #self.setArmAngle(int(commands[5]))
            elif commands[1].strip() == 'ROTATE':
                self.rotate(float(commands[2]),float(commands[3]))
                #self.setClawAngle(int(commands[4]))
                #self.setArmAngle(int(commands[5]))