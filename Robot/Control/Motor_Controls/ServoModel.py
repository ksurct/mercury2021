from adafruit_servokit import ServoKit
kit = ServoKit(channels = 8)

import adafruit_motor.servo

#   sudo pip3 install adafruit-circuitpython-pca9685
#   sudo pip3 install adafruit-circuitpython-servokit


class ServoModel():
    '''
    Class to contain servo model and presets and to move servo.
    '''

    def __init__(self,name,channel,presetDict={'home':0},minAngle=0,maxAngle=180):
        #self.servo = kit.servo[channel]
        self.servo = adafruit_motor.servo.Servo(channel)
        self.name = name
        self.presetDict = presetDict
        self.minAngle = minAngle
        self.maxAngle = maxAngle

        self.servo.actuation_angle = maxAngle   #set max angle in the kit.servo controller
    
    def updateAbsoluteAngle(self,angle):
        #Ensure angle remains in the range
        if angle < self.minAngle:
            angle = self.minAngle
        elif angle > self.maxAngle:
            angle = self.maxAngle

        #Set angle on physical servo
        self.servo.angle = angle

    def updateRelativeAngle(self,angle):
        self.updateAbsoluteAngle(self.currentAngle + angle)

    def moveToPreset(self,presetKey):
        self.updateAbsoluteAngle(self.presetDict[presetKey])


if __name__ == "__main__":
    testServo = ServoModel('testServo',0)

    userinput = 100
    print('Enter Angle(enter -1 to exit)')
    while userinput != -1:
        testServo.updateAbsoluteAngle(userinput)
        userinput = int(input())
