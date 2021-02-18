import pyglet
import sys
import os

from mercury.simulation.visualizer import Visualizer
from mercury.simulation.ObstacleGenerator import ObstacleGenerator

class SimRobotControl():
    def __init__(self, callback, rate, errorPercent):
        pyglet.clock.schedule_interval(callback, rate)
        ob = ObstacleGenerator()
        ob.generate()
        self.vis = Visualizer(ob.cornerarray, errorPercent)

    #A manual function for overriding the Model control
    def setMotorSpeed(self, motorIndex, speed):
        raise Exception("Not implemented")

    #Sets all the speeds of all the motors
    def setAllMotorSpeeds(self, motor0, motor1, motor2, motor3):
        raise Exception("Not implemented")

    #Gets the probable point
    def getProbablePoint(self):
        return [self.vis.robit.x, self.vis.robit.y]

    #Gets the probable theta
    def getProbableTheta(self):
        return self.vis.robit.theta

    #Moves the robot forward a distance at a certain speed
    def move(self, meters, speed):
        self.vis.moveForward(meters)

    #Rotates the robot by degrees at speed
    def rotate(self, degrees, speed):
        self.vis.setΘReltive(degrees) 

    def getSensorData(self):
        return self.vis.getSensorData()

    def tick(self, function):
        function(self)

if (__name__ == "__main__"):
    r = None
    PI = 3.14
    def callback(test):
        #print(test)
        #time.sleep(.25)
        
        empty = False
        r.rotate(0, 0)
        x = r.getSensorData()
        highRight = x[0]
        highLeft = x[1]
        lowLeft = x[2]
        lowRight = x[3]
        frontRight = x[4]
        frontLeft = x[5]
        frontMid = x[6]

        #print out what the sensors are detecting for testing purposes
        measures = str(highRight[0]) + highRight[1] + "   " + str(lowRight[0]) + lowRight[1]+ "   " + str(highLeft[0]) + highLeft[1] + "   " + str(lowLeft[0]) + lowLeft[1] + "   " + str(frontRight[0]) + frontRight[1] + "   " + str(frontMid[0]) + frontMid[1] + "   " + str(frontLeft[0]) + frontLeft[1]
        #print(measures)
        
        #If nothing is detected in front of the robot
        if (frontRight[0] == empty and frontLeft[0] == empty and frontMid[0] == empty):
            
            print("forward")
            r.move(10,0)
            print(r.getProbableTheta())
        #something is in front a front facing sensors
        else: 
            #if there is nothing to the right, rotate right
            if (highRight[0] == empty and lowRight[0] == empty):
                print("right")
                r.rotate(PI/2, 0)
                print(r.getProbableTheta())
            #if something is to the right, see if you can rotate left
            elif (highLeft[0] == empty and lowLeft[0] == empty):
                print("left")
                r.rotate(-PI/2,0)
                print(r.getProbableTheta())
            #if there is something to both right and left, go backwards and then try to rotate 
            else:
                print("reverse")
                r.rotate(PI, 0)
                print(r.getProbableTheta())


    r = SimRobotControl(callback, 0.1, 0)

    pyglet.app.run()