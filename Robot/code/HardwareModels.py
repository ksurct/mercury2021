"""
    This file will contain models for all hardware used on the robot
    Each model will hold code to control one hardware component we have on the robot
    One instance of a model will hold info for one piece of hardware
"""

import RPi.GPIO as GPIO
import Adafruit_PCA9685 as PCA

GPIO.setmode(GPIO.BOARD)

"""
    This model is for drive motors on the robot
"""
class MotorModel:
    """
        Construtor to create an instance of a motor
        Takes in the following parameters:
            Controller button/joystick that moves the motor forward/backward
            PWM pin it should output to in order to move the motor
            Direction output pin to tell the board which direction to move in
    """
    def __init__(self, initiationDict: dict):
        try:
            self.controllerInput = initiationDict['controllerInput']
            self.outputPWMPin = initiationDict['outputPWMPin']
            self.directionPin = initiationDict['directionPin']
            self.isReverse = False
            self.initReverse = initiationDict['initReverse']
            self.name = initiationDict['name']
            self.motorSpeed = 0
            GPIO.setup(self.outputPWMPin, GPIO.OUT) #initialize PWM pin
            GPIO.setup(self.directionPin, GPIO.OUT) #initialize direction pin
            GPIO.output(self.directionPin, 0 if self.initReverse == True else 1) #set direction to forward to start
            self.motorPWM = GPIO.PWM(self.outputPWMPin, 100) #set up PWM wave on motor pin
            self.motorPWM.start(0) #start PWM tracking
        except KeyError as err:
            print(err)
            raise
        
    def __del__(self):
        self.motorPWM.stop()

    def move(self, controllerInputValue: int) -> int:
        #TODO Move the motor
        print("Name is {} and value is {}".format(self.name, controllerInputValue))
        if (controllerInputValue < 0):
            if not self.isReverse:
                #We want to be reverse but currently are not
                GPIO.output(self.directionPin, 1 if self.initReverse == True else 0)
                self.isReverse = True
            controllerInputValue *= -1 #always need to give a positive value to ChangeDutyCycle
        elif (controllerInputValue > 0 and self.isReverse):
            #Want to go forward but currently going backward
            GPIO.output(self.directionPin, 0 if self.initReverse == True else 1)
            self.isReverse = False
        if (self.motorSpeed / 10 != controllerInputValue):
            self.motorSpeed = controllerInputValue * 10 #update current speed
            self.motorPWM.ChangeDutyCycle(self.motorSpeed) #actually change PWM value to motor board
        return self.motorSpeed

    def getControlInput(self) -> str:
        return self.controllerInput

class MotorDriverModel:
    def __init__(self):
        pass

    def moveMotors(self):
        pass

    def getControlInput(self):
        pass

class ServoModel:
    """
        Construtor to create an instance of a servo
        Takes in the following parameters:
            Controller button/joystick that moves the motor forward/backward
            Channel is the channel on the breakout board that the servo plugs into
            Maximum PWM value it should be at
            Minimum PWM value it should be at
    """
    def __init__(self, initiationDict: dict):
        try:
            self.controllerInput = initiationDict['controllerInput']
            self.minValue = initiationDict['minValue']
            self.maxValue = initiationDict['maxValue']
            self.channel = initiationDict['channel']
            self.servoPosition = 0
        except KeyError as err:
            print(err)
            raise

    def move(self, controllerInputValue: int) -> int:
        #TODO move the servo
        return self.servoPosition

    def getControlInput(self) -> str:
        return self.controllerInput

class SensorModel:
    def __init__(self):
        pass


if __name__ == '__main__':
    x = MotorModel({'controllerInput':'a', 'outputPWMPin':1})
    y = ServoModel({'controllerInput':'a', 'minValue':0, 'maxValue':100, 'outputPWMPin':1})