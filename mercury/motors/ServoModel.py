from adafruit_servokit import ServoKit
kit = ServoKit(channels = 8)

class ServoModel():

    def __init__(self,name,channel,minPWM,maxPWM):

        self.servo = kit.servo[channel]
        self.name = name
        self.minPWM = minPWM
        self.maxPWM = maxPWM
    
    def updateAbsoluteAngle(self,angle):
        if (angle < 181 or angle > -1): 
            self.servo.angle = angle
        

if __name__ == "__main__":
    testServo = ServoModel('testServo',0,0,250)

    userinput = 100
    print('Enter Angle(enter -1 to exit)')
    while userinput != -1:
        testServo.updateAbsoluteAngle(userinput)
        userinput = int(input())
