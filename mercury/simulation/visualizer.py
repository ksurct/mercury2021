import pyglet
from math import *
import sys
import os

#TODO: This is the code that must be updated to the new module system
#TODO: Replace this robot model with the brand new one, be careful to update accordingly

from mercury.simulation.RobotModel import RobotModel
from mercury.simulation.ObstacleGenerator import ObstacleGenerator
PI = pi
main_batch = pyglet.graphics.Batch() # collects all drawings to display


class Visualizer():
    def __init__(self, boxes, error):
        self.boxes = boxes
        self.scale = 10 # scales the generated field to create more detail
        self.robit = RobotModel("type", error, 13 * self.scale, 15 * self.scale)
        self.window = pyglet.window.Window(width=96 * self.scale, height=72 * self.scale)
        self.PsuedoRayCast = PsuedoRayCast(self.window, self.boxes, self.scale)
        self.Θ1 = atan(self.robit.length / self.robit.height)
        self.d = sqrt((self.robit.length/2)**2 + (self.robit.height/2)**2)

        # this is just to calculate 
        self.sensors = [
            (sqrt((self.robit.length/2)**2 + (1*self.robit.height/2)**2), atan((self.robit.length) / (self.robit.height)), PI / 2, "Right Top"), # right top
            (sqrt((self.robit.length/2)**2 + (1*self.robit.height/2)**2), -atan((self.robit.length) / (self.robit.height)), -PI / 2, "Left Top"), # Left top
            (sqrt((self.robit.length/2)**2 + (1*self.robit.height/2)**2), PI + atan((self.robit.length) / (self.robit.height)), -PI / 2, "Left bottom"), # Left bottom
            (sqrt((self.robit.length/2)**2 + (1*self.robit.height/2)**2), -PI + -atan((self.robit.length) / (self.robit.height)), PI / 2, "Right Bottom"), # right bottom
            (sqrt((self.robit.length/3)**2 + (1*self.robit.height/2)**2), atan((self.robit.length) / (self.robit.height)), 0, "Front Right"),
            (sqrt((self.robit.length/3)**2 + (1*self.robit.height/2)**2), -atan((self.robit.length) / (self.robit.height)), 0, "Front Left"),
            (sqrt((self.robit.length/2)**2 + (1*self.robit.height/4)**2), 0, 0, "Front Middle")
        ]
        self.setXYAbsolute(0, 462)
        self.setΘAbsolute(PI/2)

    """
  (g, h)     |Θ    (a,b)
    _________|________
    |        |      /|
    |        |     / |                  
    |      r ---> /  |
    |        |   /   |
    |        |Θ1/    |
    |        | /     |
    |        |/      |
    |      (x, y)    |
    |                |
    |                |
    |                |
    |                |
    |________________|
  (e, f)            (c, d)
    """
    def drawBoxAtAngle(self, x, y, r, Θ, Θ1): # simply draws a box at an angle acording to above diagram
        global main_batch
        (a, b) = self.getPointOnBox(x, y, r, Θ, Θ1, 1) # use all corners to generate box
        (c, d) = self.getPointOnBox(x, y, r, Θ, Θ1, 2)
        (e, f) = self.getPointOnBox(x, y, r, Θ, Θ1, 3)
        (g, h) = self.getPointOnBox(x, y, r, Θ, Θ1, 4)
        main_batch.add(8, pyglet.gl.GL_LINES, None, ("v2f", ( # generate box
            e, f, c, d, # e, f -> c, d
            e, f, g, h, # e. f -> g, h
            g, h, a, b, # g, h -> a, b
            c, d, a, b, # c, d -> a, b
        )))

    """
    Relative x and y: where the box is centered
    d: distance to one corner
    Θ: the orientation of the box
    Θ1: the angle the crossline makes with the square's relative perpendicular y axis see above diagram
    quadrent: The quadrent
    """
    def getPointOnBox(self, x, y, d, Θ, Θ1, quadrent): # gets a corner of the box based on above
        if (quadrent == 1):
            return ((d*sin(Θ + Θ1) + x), (d*cos(Θ + Θ1) + y))
        if (quadrent == 2):
            return ((d*sin(Θ - Θ1 + PI) + x), (d*cos(Θ - Θ1 + PI) + y))
        if (quadrent == 3):
            return ((self.d*sin(Θ + Θ1 + PI) + x), (d*cos(Θ + Θ1 + PI) + y))
        if (quadrent == 4):
            return ((self.d*sin(Θ - Θ1) + x), (self.d*cos(Θ - Θ1) + y))
        
    def drawSquare(self, a, b, c, d):
        global main_batch
        main_batch.add(8, pyglet.gl.GL_LINES, None,
                            ('v2f', (a, b, c, b, a,b,a,d, c,b,c,d, a,d,c,d),
                        ))

    def drawAllBoxes(self):
        if (not self.boxes):
            return
        print(len(self.boxes))
        for box in self.boxes:
                self.drawSquare(box[0][0] * self.scale, box[0][1] * self.scale, box[1][0] * self.scale, box[1][1] * self.scale)


    def redraw(self):
        print("redraw")
        self.window.clear()
        global main_batch
        main_batch = pyglet.graphics.Batch()
        self.drawAllBoxes()
        self.drawBoxAtAngle(self.robit.x, self.robit.y, self.d, self.robit.theta, self.Θ1)
        if (__name__ == '__main__'):
            self.runAllSensors()
        main_batch.draw()

    def getSensorData(self):
        data = []
        for sensor in self.sensors:
            (a, b) = self.getSenorPoint(sensor)
            distance = self.PsuedoRayCast.rayCast(a, b, self.robit.theta + sensor[2])
            #data.append((distance / self.scale, sensor[3]))
            if (distance != None and distance > 0):
                data.append((distance / self.scale, sensor[3]))
            #if there is no sensor data, set distance as -34404 (reminded me of ERROR)
            else:
                data.append((False, sensor[3]))        
        return data

    def runAllSensors(self):
        for sensor in self.sensors:
            (a, b) = self.getSenorPoint(sensor)
            distance = self.PsuedoRayCast.rayCast(a, b, self.robit.theta + sensor[2])
            if (distance):
                print(sensor[3] + " ", distance / self.scale, "in")
            else:
                print(sensor[3] + " ?in")

    def getSenorPoint(self, sensor):
        return (self.robit.x + sensor[0] * sin(sensor[1] + self.robit.theta), self.robit.y + sensor[0] * cos(sensor[1] + self.robit.theta))
    
    def setXYAbsolute(self, x, y):
        self.robit.x = x
        self.robit.y = y
        self.redraw()

    def setΘAbsolute(self, Θ):
        self.robit.theta = Θ
        self.redraw()

    def setXYRelative(self, x, y):
        self.robit.x = self.robit.x + x
        self.robit.y = self.robit.y + y
        self.redraw()

    def setΘReltive(self, Θ):
        self.robit.theta = self.robit.theta + Θ
        self.redraw()

    def moveForward(self, x):
        self.robit.moveDistance(x)
        self.redraw()

    def radToDeg(self, Θ):
        return (180 / PI) * Θ
    def degToRad(self, Θ):
        return (PI / 180) * Θ

    def getFrontSensorPoint(self):
        return (sin(self.robit.theta)*self.robit.height // 2 + self.robit.x, cos(self.robit.theta)*self.robit.height // 2 + self.robit.y)

    def getFrontSensorData(self):
        return self.getFrontSensorPoint()


class PsuedoRayCast():
    def __init__(self, window, boxes, minDistance): # takes in a pyglet window objectalison
        self.scale = 0.25
        self.debug = False
        self.minDistance = minDistance * self.scale
        self.window = window
        self.maxDistance = 100
        self.boxes = boxes

    def getLineFunction(self, a, b, Θ):
        if (abs(sin(Θ)) > sqrt(2)/ 2): # if it is above the 45 degree mark a function in terms of x is more usesful
            return (lambda x: (1/tan(Θ) if tan(Θ) != 0 else 0)*(x - a) + b, "x")
        else:
            return (lambda y: (tan(Θ))*(y - b) + a, "y")
    def rayCast(self, a, b, Θ):
        (f, withRespectTo) = self.getLineFunction(a,b,Θ)
        mod = (-1 if sin(Θ) < 0 else 1) if withRespectTo == "x" else (-1 if cos(Θ) < 0 else 1)
        i = a if withRespectTo == "x" else b
        while(i < (self.window.width if withRespectTo == "x" else self.window.height) and i > 0 and f(i) > 0 and f(i) < (self.window.height if withRespectTo == "x" else self.window.width)):
            i = i + self.minDistance * mod
            if (sqrt((i - a)**2 + (f(i) - b)**2) > self.maxDistance if withRespectTo == "x" else sqrt((f(i) - a)**2 + (i - b)**2) > self.maxDistance):
                return 0
            if (self.checkPoint(i, f(i)) if withRespectTo == "x" else self.checkPoint(f(i), i)):
                return sqrt((i - a)**2 + (f(i) - b)**2) if withRespectTo == "x" else sqrt((f(i) - a)**2 + (i - b)**2)
            
    def checkPoint(self, a, b):
        global main_batch
        if (self.debug):
            main_batch.add(1, pyglet.gl.GL_POINTS, None,
            ('v2f', (a, b)),
            ('c3B', (255, 255, 0)))
        for box in self.boxes:
            if (((box[0][0]*self.minDistance/self.scale <= a and box[1][0]*self.minDistance/self.scale >= a) or (box[0][0]*self.minDistance/self.scale >= a and box[1][0]*self.minDistance/self.scale <= a)) 
            and ((box[0][1]*self.minDistance/self.scale <= b and box[1][1]*self.minDistance/self.scale >= b) or (box[0][1]*self.minDistance/self.scale >= b and box[1][1]*self.minDistance/self.scale <= b))
            ):
                return True
        
        return False
ob = None
vis = None
if (__name__ == '__main__'):
    ob = ObstacleGenerator()
    ob.generate()
    vis = Visualizer(ob.cornerarray, 0)
    @vis.window.event
    def on_key_press(key, mod):
        # print("point: ", vis.robot.position)
        key = chr(key)
        if (key == 'a'):
            vis.setXYRelative(-10, 0)
        if (key == 's'):
            vis.setXYRelative(0, -10)
        if (key == 'd'):
            vis.setXYRelative(10, 0)
        if (key == 'w'):
            vis.setXYRelative(0, 10)
        if (key == 'p' or key == 'ｓ'):
            vis.setΘReltive(PI/24) 
        if (key == 'o' or key == 'ｑ'):
            vis.setΘReltive(-PI/24) 
        if (key == 'ｔ'):
            vis.moveForward(-10)
        if (key == 'ｒ'):
            vis.moveForward(10)
        print(vis.robit.x, vis.robit.y)
        print(key)
        # print(vis.getFrontSensorData())
    pyglet.app.run()
