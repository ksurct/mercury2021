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
        #print("Name is {} and value is {}".format(self.name, controllerInputValue))
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
        if (self.motorSpeed / 10 != controllerInputValue): #if we are not currently going the speed we want to be going
            self.motorSpeed = controllerInputValue * 10 #update current speed
            self.motorPWM.ChangeDutyCycle(self.motorSpeed) #actually change PWM value to motor board
        return self.motorSpeed #probably don't need to return anything, but here it is just in case

    def getControlInput(self) -> str:
        return self.controllerInput

"""
    This model represents one of the motor driver boards we have on the robot
    Using this model assumes that the two motors it is controlling are on the same side of the robot
        (Two left wheels connected to a board, two right wheels connected to a board)
    This also assumes that we want the two motors on the same side of the robot to move at the same speed in the same direction, which should always be true
    The main purpose of this class is to cut the number of calls to change motor positions in half
    By using this, we only need to tell the motor board to change the motor positions instead of telling each of the two motors to change positions
"""
class MotorDriverModel:
    def __init__(self, motorsList, controllerInput):
        self.motors = []
        self.controllerInput = controllerInput
        for i in motorsList:
            self.motors.append(MotorModel(i))

    def moveMotors(self, controllerValue):
        for motor in self.motors:
            motor.move(controllerValue)

    def getControlInput(self):
        return self.controllerInput

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
    print("No need to call this class as main, it just holds other classes")