import RPi.GPIO as GPIO

class Motor():
    @staticmethod
    def getDefaultMotors():
        return [Motor(18, 20, "LEFT", 1),
        Motor(12, 21, "LEFT", 1),
        Motor(13, 5, "RIGHT", 1),
        Motor(19, 6, "RIGHT", 1)]
    
    # The modifier can be used to correct a motor, 
    # if it is too fast compared to others
    # NOTE: We may need to implement a modifier function
    # if the motor behavior is not linear.
    def __init__(self, pwmPin, dirPin, name, modifier):
        self.modifier = modifier
        self.speed = 0
        self.name = name
        self.dir = 1
        GPIO.setup(pwmPin, GPIO.OUT)
        GPIO.setup(dirPin, GPIO.OUT)
        self.pwmPin = GPIO.PWM(pwmPin, 1000)
        self.pwmPin.ChangeDutyCycle(100)
        self.pwmPin.start(0)
        self.dirPin = dirPin

    # TODO: This function will set the speed of the motors, but will do so
    # in a non-blocking fashion. This is needed so that all motors can be 
    # set at once.    
    def setSpeedSmooth(self, speed, other):
        pass

    def setSpeed(self, speed):
        self.speed = speed
        if (speed < 0):
            self.setDirection(-1)
        else:
            self.setDirection(1)
        self.pwmPin.ChangeDutyCycle(abs(speed * self.modifier))
    
    def setDirection(self, dir):
        self.dir = dir
        # 1 is F -1 is back
        GPIO.output(self.dirPin, GPIO.LOW if self.dir == 1 else GPIO.HIGH)
            
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

if (__name__ == "__main__"):
    M1 = Motor(18, 24,"",1)
    M2 = Motor(12, 7,"",1)
    M3 = Motor(13, 5,"",1)
    M4 = Motor(26, 6,"",1)

    M1.setSpeed(50)
    M2.setSpeed(0)
    M3.setSpeed(0)
    M4.setSpeed(0)
