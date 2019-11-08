from math import cos, sin, pi
import numpy as np
import random






class RobotModel:

    def __init__(self, type, errorPercent):
        self.type = type
        self.length = .01
        self.errorPercent = errorPercent
        self.x = 0
        self.y = 0
        self.theta = 0
        self.dt = .01

    def moveFK(self, vR, vL, t):

        w = (vR-vL)/self.length
        steps = t/self.dt

        if (vR != vL):
            R = (self.length/2) * (vR+vL) / (vR-vL)
            print(R)

            for i in range(int(steps)):
                ICC = [(self.x-R*cos(w*self.dt)) , (self.y+R*sin(w*self.dt))]

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

                mX = np.dot(mA,mB) + mC

                self.x = float(mX[0])
                self.y = float(mX[1])
                self.theta = float(mX[2]) % (2 * pi)

        else:
            for i in range(int(steps)):
                self.x += vR * self.dt * cos(self.theta)
                self.y += vL * self.dt * sin(self.theta)

        print("x = ", self.x)
        print("y = ", self.y)
        print("theta = ", self.theta)
        print("moved")

    def giveError(self, number):
        return number * (1 + ((random() % (self.errorPercent + 1)) * (random() % 2 == 0 ? -1 : 1)) / 100)

    def moveTheta(self, radians):
        self.theta = giveError(self.theta + radians)

    def moveDistance(self, meters):
        self.x = giveError(cos(self.theta)*meters + self.x)
        self.y = giveError(sin(self.theta)*meters + self.y)

model = RobotModel("type")
model.moveFK(1,-1,10)
