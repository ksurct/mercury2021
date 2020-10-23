class motor():
    def __init__(self, PWMpin, DIRpin):
        self.speed = 0
        self.FORWARD = 1
        self.BACK = 0
        self.dir = self.FORWARD
        GPIO.setup(PWMpin, GPIO.OUT)
        GPIO.setup(DIRpin, GPIO.OUT)
    
    def setSpeed(self, speed):
        self.speed = speed
    
    def direction(self, FORWARD, BACK):
        if(FORWARD = True):
            self.dir = self.FORWARD
        else:
            self.dir = self.BACK
            
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)