from math import cos, sin, pi
import numpy as np
import random






class RobotModel:

    def __init__(self, type, errorPercent, l):
        self.type = type
        self.length = l
        self.errorPercent = errorPercent
        self.x = 0
        self.y = 0
        self.theta = 0
        self.dt = .001

    def moveFK(self, vR, vL, t):

        steps = t/self.dt   #calculate number of steps to execute

        if (vR != vL):      #if vR and vL are different
                                #calculate radius of curvature of the robots path
                                #calculate angular velocity of robot
                                #calculate instantaneous center of rotation
            R = (self.length/2) * ((vR+vL) / (vR-vL))
            w = (vR-vL)/self.length
            ICC = [(self.x-R*sin(self.theta)) , (self.y+R*cos(self.theta))]

            for i in range(int(steps)):     #for each step
                                                #calculate new x, y, theta
                #ICC = [(self.x-R*cos(self.theta)) , (self.y+R*sin(self.theta))]

                A = [[cos(w*self.dt) , -sin(w*self.dt) , 0],
                     [sin(w*self.dt) ,  cos(w*self.dt) , 0],
                     [             0 ,               0 , 1]]

                B = [[self.x - ICC[0]],
                     [self.y - ICC[1]],
                     [     self.theta]]

                C = [[ICC[0]   ],
                     [ICC[1]   ],
                     [w*self.dt]]

                mA = np.array(A)
                mB = np.array(B)
                mC = np.array(C)

                mX = mA.dot(mB) + mC

                self.x = float(mX[0])
                self.y = float(mX[1])
                self.theta = float(mX[2]) % (2 * pi)

        else:
            for i in range(int(steps)):
                self.x += vR * self.dt * cos(self.theta)
                self.y += vR * self.dt * sin(self.theta)

        print("Moving Robot")
        print("new x = ", self.x)
        print("new y = ", self.y)
        print("new theta = ", self.theta)
        print("moved")

    def giveError(self, number):
        return number * (1 + ((random() % (self.errorPercent + 1)) * (-1 if random() % 2 == 0 else 1)) / 100)

    # for the algos to run
    def moveDistance(self, meters):
        self.x = giveError(cos(self.theta)*meters + self.x)
        self.y = giveError(sin(self.theta)*meters + self.y)

    # for the algos to run
    def moveTheta(self, radians):
        self.theta = giveError(self.theta + radians)

    # this is to be used by the robot
    def wheelSpeedToMoveInCircleOfRadiusAndInWhatTime(self, radius, period):
        omega = period / (2 * pi)
        vRight = omega * (radius + self.length / 2)
        vLeft = omega * (radius - self.length / 2)
        return {"rightVelocity": vRight, "leftVelocity": vLeft}

    # for the actual robot to run
    def timeAtAVelocityToTurnTheta(self, radians, metersPerSecond):
        return ((self.theta) / (2 * metersPerSecond)) * self.length
    def timeAtAVelocityToGoMeters(self, meters, metersPerSecond):
        return (meters / metersPerSecond)
model = RobotModel("type", 0, 1)
model.moveFK(1,2,10)
