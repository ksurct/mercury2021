class Motor():
    @staticmethod
    def getDefaultMotors():
        return [Motor(18, 20, "LEFT", 1),
        Motor(12, 21, "LEFT", 1),
        Motor(13, 5, "RIGHT", 1),
        Motor(19, 6, "RIGHT", 1)]
        
    def __init__(self, pwmPin, dirPin, name, modifier):
        self.modifier = modifier
        self.name = name
        self.speed = 0
        self.dir = 1
    
    def setSpeed(self, speed):
        self.speed = speed
        if (speed < 0):
            self.setDirection(-1)
        else:
            self.setDirection(1)

        print("Set speed of Motor ", self.name)
    
    def setDirection(self, dir):
        self.dir = dir            