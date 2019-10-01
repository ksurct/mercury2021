import random
from Point import Point
from ObstacleField import *

class ObstacleGenerator:

    def __init__(self):

        self.lengths = [12, 12, 24, 24, 36]
        self.maxx = 96
        self.maxy = 72
        self.points = []
        self.pointobjects = []
        #self.array = [[0] * self.maxx] * self.maxy
        self.array = []

    def checkCollisions(self, obstaclepoints, points):

        for obstaclepoint in obstaclepoints:
            #print(obstaclepoint)
            for point in points:
                if (point == obstaclepoint):
                    #print('Fail Collision')
                    return True
            if ((obstaclepoint[0] < 0) or (obstaclepoint[0] > self.maxx)):
                #print('Fail x-bound')
                return True
            elif ((obstaclepoint[1] < 0) or (obstaclepoint[1] > self.maxy)):
                #print('Fail y-bound')
                return True

            #else:
                #print('Success')
        return False


    def convertToArray(self):


        self.array.append([])
        for j in range(self.maxy): #y
            self.array.append([])
            for i in range(self.maxx): #x
                self.array[j].append(0)
        self.array.pop()

        for point in self.points:
            self.array[point[1]][point[0]] = 1

        for i in self.array:
            print(i)


    def generate(self):

        pathcheck = True

        while (pathcheck):
            for length in self.lengths:

                collision = True
                while (collision == True):
                    initpoint = (random.randint(0,self.maxx-1),random.randint(0,self.maxy-1))
                    direction = random.randint(0,3) # 0,1,2,3  ::  E,N,W,S

                    obstaclepoints = []

                    if (direction == 0): #East

                        for i in range(length):
                            obstaclepoints.append( (initpoint[0] + i, initpoint[1]) )
                            obstaclepoints.append( (initpoint[0] + i, initpoint[1] + 1) )

                    elif (direction == 1): #North

                        for i in range(length):
                            obstaclepoints.append( (initpoint[0], initpoint[1] + i) )
                            obstaclepoints.append( (initpoint[0] + 1, initpoint[1] + i) )

                    elif (direction == 2): #West

                        for i in range(length):
                            obstaclepoints.append( (initpoint[0] - i, initpoint[1]) )
                            obstaclepoints.append( (initpoint[0] - i, initpoint[1] + 1) )

                    elif (direction == 3): #South

                        for i in range(length):
                            obstaclepoints.append( (initpoint[0], initpoint[1] - i) )
                            obstaclepoints.append( (initpoint[0] + 1, initpoint[1] - i) )


                    #Check if points collide with other obstacles or walls
                    collision = self.checkCollisions(obstaclepoints, self.points)

                    if (collision == False):
                        self.points = self.points + obstaclepoints


            self.convertToArray()

            pathcheck = False

            self.points.sort()
            print(self.points)

            for point in self.points:
                self.pointobjects.append(Point(point[0],point[1]))

course = ObstacleGenerator()
course.generate()

field = ObstacleField(72, 96, 24, 34, 24, 6, course.pointobjects)
field.toString()
