"""
    This file will contain models for all hardware used on the robot
    Each model will hold code to control one hardware component we have on the robot
    One instance of a model will hold info for one piece of hardware
"""

from abc import ABC, abstractmethod

"""
    This is the abstract method that each hardware model we use will inherit
    This means that all models inheriting this class must have the same methods that this class does
"""
class MotorServoModel(ABC):
    """
        This is the constructor that each model must have
        It has a reference to itself, plus a dictionary that will hold all initial values for the variables the model has
        We use a dictionary in case two different models need different variable values
    """
    @abstractmethod
    def __init__(self, initialDict: dict):
        pass

    """
        This method will move the motor or servo, depending on what the value of controllerInputValue is
        It will return the new value of the motor/servo just in case that is needed somewhere
    """
    @abstractmethod
    def move(self, controllerInputValue: int) -> int:
        pass

    """
        This method will return what controller input value moves the motor or servo
    """
    @abstractmethod
    def getControlInput(self) -> str:
        pass

"""
    This model is for drive motors on the robot
"""
class MotorModel(MotorServoModel):
    """
        Construtor to create an instance of a motor
        Takes in the following parameters:
            Controller button/joystick that moves the motor forward/backward
            PWM pin it should output to in order to move the motor
    """
    def __init__(self, initiationDict: dict):
        try:
            self.controllerInput = initiationDict['controllerInput']
            self.outputPWMPin = initiationDict['outputPWMPin']
            self.reverse = False
            self.motorSpeed = 0
        except KeyError as err:
            print(err)
            raise

    def move(self, controllerInputValue: int) -> int:
        #TODO Move the motor
        return self.motorSpeed

    def getControlInput(self) -> str:
        return self.controllerInput

class ServoModel(MotorServoModel):
    """
        Construtor to create an instance of a servo
        Takes in the following parameters:
            Controller button/joystick that moves the motor forward/backward
            PWM pin it should output to in order to move the motor
            Maximum PWM value it should be at
            Minimum PWM value it should be at
    """
    def __init__(self, initiationDict: dict):
        try:
            self.controllerInput = initiationDict['controllerInput']
            self.minValue = initiationDict['minValue']
            self.maxValue = initiationDict['maxValue']
            self.outputPWMPin = initiationDict['outputPWMPin']
            self.servoPosition = 0
        except KeyError as err:
            print(err)
            raise

    def move(self, controllerInputValue: int) -> int:
        #TODO move the servo
        return self.servoPosition

    def getControlInput(self) -> str:
        return self.controllerInput

x = MotorModel({'controllerInput':'a', 'outputPWMPin':1})
y = ServoModel({'controllerInput':'a', 'minValue':0, 'maxValue':100, 'outputPWMPin':1})