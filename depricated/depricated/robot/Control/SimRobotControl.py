import pyglet
import sys
import os
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + "/../../Test/PygletSim/")
from Visualizer import Visualizer
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + "/../../Test/")
from ObstacleGenerator import ObstacleGenerator
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
        print(test)
        r.move(10, 0);    
        r.rotate(0, 0)
    r = SimRobotControl(callback, 0.1, 0.01)

    pyglet.app.run()