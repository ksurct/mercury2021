from adafruit_servokit import ServoKit
try:
    kit = ServoKit(channels = 8)
except:
    pass
class ServoModel():

    def __init__(self,name,channel,minPWM,maxPWM):
        self.failed = False
        try:
            self.servo = kit.servo[channel]
            self.name = name
            self.minPWM = minPWM
            self.maxPWM = maxPWM
        except:
            print("servo init failed")
            self.failed = True
    
    def updateAbsoluteAngle(self,angle):
        if (self.failed == True):
            return
        if (angle < 181 or angle > -1): 
           self.servo.angle = angle
        

if __name__ == "__main__":
    testServo = ServoModel('testServo',0,0,250)

    userinput = 100
    print('Enter Angle(enter -1 to exit)')
    while userinput != -1:
        testServo.updateAbsoluteAngle(userinput)
        userinput = int(input())
