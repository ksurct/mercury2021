import RPi.GPIO as GPIO

class motor():
    def __init__(self, PWMpin, DIRpin):
        self.speed = 0
        self.FORWARD = 1
        self.BACK = 0
        self.dir = self.FORWARD
        GPIO.setup(PWMpin, GPIO.OUT)
        GPIO.setup(DIRpin, GPIO.OUT)
        self.PWMpin1 = GPIO.PWM(PWMpin, 1000)
        self.PWMpin1.ChangeDutyCycle(100)
        self.PWMpin1.start(0)
    
    def setSpeed(self, speed):
        self.speed = speed
        self.PWMpin1.ChangeDutyCycle(speed)
    
    def direction(self, FORWARD, BACK):
        if(FORWARD == True):
            self.dir = self.FORWARD
        else:
            self.dir = self.BACK
            
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

M1 = motor(18, 24)
M2 = motor(12, 7)
M3 = motor(13, 5)
M4 = motor(26, 6)

M1.setSpeed(0)
M2.setSpeed(0)
M3.setSpeed(0)
M4.setSpeed(0)