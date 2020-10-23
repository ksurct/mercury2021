'''
import RPi.GPIO as GPIO
import busio
try:
    import adafruit_pca9685
except:
    pass
from time import sleep
import board

i2c_bus = busio.I2C(board.SCL,board.SDA)
#GPIO.setmode(GPIO.BOARD)
'''
from adafruit_servokit import ServoKit
kit = ServoKit(channels = 8)

class ServoModel():

    def __init__(self,name,channel,minPWM,maxPWM):
        #self.pwm = adafruit_pca9685.PCA9685(i2c_bus)
        #self.pwm.frequency = 60
        
        self.servo = kit.servo[channel]
        
        self.name = name
        
        
        #self.channel = channel
        #self.presetDict = presetDict
        self.minPWM = minPWM
        self.maxPWM = maxPWM

        #self.currentPWM = 100
        #self.currentAngle = self.calcAnglefromPWM(self.currentPWM)

        #self.pwm.set_pwm(self.channel, 0, self.currentPWM)
    '''
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
        self.currentAngle = self.calcAnglefromPWM(self.currentPWM)'''

    def updateRelativeAngle(self,angle):
        finalAngle = self.currentAngle + angle
        finalPWM = self.calcPWMfromAngle(finalAngle)
        self.updatePWM(finalPWM)
    
    def updateAbsoluteAngle(self,angle):
        '''finalPWM = self.calcPWMfromAngle(angle)
        self.updatePWM(finalPWM)'''
        self.servo.angle = angle

if __name__ == "__main__":
    testServo = ServoModel('testServo',0,0,250)

    userinput = 100
    print('Enter Angle(enter -1 to exit)')
    while userinput != -1:
        testServo.updateAbsoluteAngle(userinput)
        userinput = int(input())
