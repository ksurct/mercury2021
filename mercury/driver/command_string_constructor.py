
class CommandStringConstructor():
    def __init__(self):
        self.leftSpeed = 0
        self.rightSpeed = 0
        self.clawAngle = 90
        self.armAngle = 90

    def normalizeSpeed(self, speed):
        if (abs(speed) > 100):
            speed = 100 * (speed / abs(speed))
        return speed

    def normalizeAngle(self, angle):
        #TODO: find actual range of motion
        if (angle > 180):
            angle = 180
        if (angle < 0):
            angle = 0
        return angle

    def setLeftSpeed(self, speed):
        speed = self.normalizeSpeed(speed)
        self.leftSpeed = speed

    def setRightSpeed(self, speed):
        speed = self.normalizeSpeed(speed)
        self.rightSpeed = speed

    def setArmAngle(self, angle):
        angle = self.normalizeAngle(angle)
        self.armAngle = angle

    def setClawAngle(self, angle):
        angle = self.normalizeAngle(angle)
        self.clawAngle = angle

    def getContinuousCommand(self):
        return "CONTINUOUS, {}, {}, {}, {}".format(self.leftSpeed,self.rightSpeed,self.armAngle,self.clawAngle)