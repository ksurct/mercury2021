import RPi.GPIO as GPIO
try:
    import Adafruit_PCA9685
except:
    pass
from time import sleep

GPIO.setmode(GPIO.BOARD)

class ServoModel():

    def __init__(self,name,channel,minPWM,maxPWM):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(40)

        self.name = name
        self.channel = channel
        #self.presetDict = presetDict
        self.minPWM = minPWM
        self.maxPWM = maxPWM

        self.currentPWM = 100
        self.currentAngle = self.calcAnglefromPWM(self.currentPWM)

        self.pwm.set_pwm(self.channel, 0, self.currentPWM)

    def calcAnglefromPWM(self,PWM):
        return (90*(PWM - self.minPWM)/(self.maxPWM - self.minPWM))

    def calcPWMfromAngle(self,angle):
        return int((angle/90)*(self.maxPWM-self.minPWM)+self.minPWM)

    def updatePWM(self,PWM):
        PWM = int(PWM)
        if (PWM > self.maxPWM):
            PWM = self.maxPWM
        elif (PWM < self.minPWM):
            PWM = self.minPWM
        self.currentPWM = PWM
        self.currentAngle = self.calcAnglefromPWM(self.currentPWM)

    def updateRelativeAngle(self,angle):
        finalAngle = self.currentAngle + angle
        finalPWM = self.calcPWMfromAngle(finalAngle)
        self.updatePWM(finalPWM)
    
    def updateAbsoluteAngle(self,angle):
        finalPWM = self.calcPWMfromAngle(angle)
        self.updatePWM(finalPWM)

if __name__ == "__main__":
    testServo = ServoModel('testServo',0,0,250)

    userinput = 100
    print('Enter PWM (enter -1 to exit)')
    while userinput != -1:
        testServo.updatePWM(userinput)
        userinput = input()