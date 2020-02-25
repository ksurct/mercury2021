"""
    This file will contain models for all hardware used on the robot
    Each model will hold code to control one hardware component we have on the robot
    One instance of a model will hold info for one piece of hardware
"""

"""
    This model is for drive motors on the robot
"""
class MotorModel:
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