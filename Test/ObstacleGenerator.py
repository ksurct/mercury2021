import random
from Point import Point
from ObstacleField import *
import PathFinder

class ObstacleGenerator:

    def __init__(self):

        self.lengths = [12, 12, 24, 24, 36]     #list of obstacle lengths, # of lengths = # of obstacles
        self.maxx = 96          #x dimension
        self.maxy = 72          #y dimension
        self.points = []        #[[x1,y1],[x2,y2]....] set of occupied points
        self.pointobjects = []  #List of occupied point objects
        self.array = []         # 0 1 array describing course
        self.invertarray = []

        self.exitoffset = 6
        self.entranceoffset = 34
        self.entrancewidth = 24
        self.exitwidth = 24
        self.message = -1

    #Check if obstacles overlap eachother or outer walls
    def checkCollisions(self, obstaclepoints, points):

        #check if any point overlaps with any existing obstacle
        for obstaclepoint in obstaclepoints:
            for point in points:
                if (point == obstaclepoint):
                    return True

        #check if any point is out of bounds
            if ((obstaclepoint[0] < 0) or (obstaclepoint[0] >= self.maxx)):
                return True
            elif ((obstaclepoint[1] < 0) or (obstaclepoint[1] >= self.maxy)):
                return True

        #if there are no problems, return False, no collisions
        return False

    #convert to array for Cadens path checker
    def convertToArray(self):

        #populate empty course array with 0
        self.array = [[0 for x in range(self.maxx)] for y in range(self.maxy)]

        #populate obstaclepoints in array as 1
        for point in self.points:
            self.array[point[1]][point[0]] = 1

        for row in range(self.maxy):
            if ((row < self.exitoffset) or row >= (self.exitoffset + self.exitwidth)):
                self.array[row].insert(0,1)

            else:
                self.array[row].insert(0,0)

            if ((row < self.entranceoffset) or row >= (self.entranceoffset + self.entrancewidth)):
                self.array[row].append(1)

            else:
                self.array[row].append(0)

        self.invertarray = [[0 for a in range(len(self.array))] for b in range(len(self.array[0]))]

        for y in range(len(self.array)):
            for x in range(len(self.array[0])):
                self.invertarray[x][y] = self.array[y][x]

        '''for i in self.array:
            print(i)

        print()
        for i in self.invertarray:
            print(i)'''


    #Generate Obstacles
    def generate(self):

        pathcheck = False
        pathfinder = PathFinder.PathFinder()

        #Continue until a valid path is found
        while (not pathcheck):
            self.points = []
            #For each obstacle in lengths
            for length in self.lengths:

                collision = True

                #Continue until obstacle doesn't collide with anything
                while (collision == True):
                    initpoint = (random.randint(0,self.maxx-1),random.randint(0,self.maxy-1))       #Generate a random point
                    direction = random.randint(0,3) # 0,1,2,3  ::  E,N,W,S                          #Generate a random direction

                    obstaclepoints = []

                    if (direction == 0): #East                                                      #Generate points starting at initial point
                                                                                                    #and continue in the direction until the end of
                        for i in range(length):                                                     #the length of the obstacle
                            obstaclepoints.append( (initpoint[0] + i, initpoint[1]) )
                            obstaclepoints.append( (initpoint[0] + i, initpoint[1] + 1) )

                    elif (direction == 1): #North

                        for i in range(length):
                            obstaclepoints.append( (initpoint[0], initpoint[1] + i) )               #Generate one length
                            obstaclepoints.append( (initpoint[0] + 1, initpoint[1] + i) )           #generate a second length to make it 2 thick

                    elif (direction == 2): #West

                        for i in range(length):
                            obstaclepoints.append( (initpoint[0] - i, initpoint[1]) )
                            obstaclepoints.append( (initpoint[0] - i, initpoint[1] + 1) )

                    elif (direction == 3): #South

                        for i in range(length):
                            obstaclepoints.append( (initpoint[0], initpoint[1] - i) )
                            obstaclepoints.append( (initpoint[0] + 1, initpoint[1] - i) )



                    collision = self.checkCollisions(obstaclepoints, self.points)               #Check if points collide with other obstacles or walls

                    if (collision == False):                                                    #If no collision add the obstacle to master list
                        self.points = self.points + obstaclepoints


            #convert to array for the pathchecker
            self.convertToArray()

            pathfinder.setField(self.invertarray)
            pathfinder.debug = False;
            pathfinder.setSleep(0.02)
            pathcheck = pathfinder.checkField()

            #pathcheck = True
            self.points.sort()
            #print(self.points)

            #Convert points list into a list of point objects for obstacle field
        for point in self.points:
            self.pointobjects.append(Point((point[0]+1),(point[1]+1)))


course = ObstacleGenerator()
course.generate()


field = ObstacleField(72, 96, 24, 34, 24, 6, course.pointobjects)
field.toString()
