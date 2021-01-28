from time import sleep
import os
class PathFinder(object):
    """docstring for PathFinder."""

    def __init__(self):
        self.point = False # its false not a point
        self.width = 24 #box width
        self.debug = False # displays the pathfind visually
        self.sleep = 0.5 # used to limit the speed for debugging purposes (seconds)
        self.message = -1 # displayed after each point is moved when debugging (-1 for nothing)

    def setSleep(self, new): # used to set sleep from the outside
        self.sleep = new

    def setField(self, field): # just used to set the testing field from the outside
        self.field = field 
        '''betterField =  [[0 for i in range(len(field))] for j in range(len(field[0]))]

        for x in range(0, len(field[0])):
            for y in range(0, len(field)):
                betterField[x][y] = field[y][x]
        field = betterField'''

        self.xMax = len(self.field)
        self.yMax = len(self.field[0])

    def findStart(self): # find the first valid starting point for box
        for x in range(0, len(self.field[0])):
            if self.isValid([0,x]):
                return [0,x]
        return False

    def checkField(self):
        self.point = self.findStart() # find a starting point
        if (not self.point):
            return False # it didnt even find a findStart
        # do the 'algo rythem' now
        self.setPoint(self.point)
        return self.moveForeward()

    def moveForeward(self):
        stack = []; # stack of 'last valid points' 
        used = []; #used points
        while True:
            overideDown = False
            if (not self.moveForwardIsValid(self.point)): # need to run obsticle avoidance
                if (self.point not in used): # if not used
                    stack.append(self.point) #store for later failure
                    used.append(self.point) # make used
                if (not overideDown and not self.downForward()):
                    if (len(stack) != 0):
                        self.point = stack.pop() # get the last valid foreward value
                    else:
                        return False;
                    succeeded = self.upForward()
                    if (not succeeded and len(stack) == 0):
                        return False
                    elif (len(stack) > 0 and not succeeded):
                        self.point = stack.pop() # if can't move up foreward and we have a stack make the self.point equal the last valid foreward point
                        overideDown = True # makes the program try goin up
                elif (overideDown):
                    overideDown = False
                    if (not self.upForward() and len(stack) == 0):
                        return False
                    elif (len(stack) > 0):
                        self.point = stack.pop()
                        overideDown = True
            self.setPoint([self.point[0] + 1, self.point[1]]) # just keep going
            if (self.isComplete(self.point)):
                print(self.point)
                if (not self.isValid(self.point)): #should never happen
                    self.debug = True;
                    self.sleep = 0.5
                    self.checkField();

                return True # the battle is won

    #these are all a set of possible moves the program will take to try and avoid an obsticle found in front of it. They all chain together to path find
    # name meaning example: down forward (tries to move down until can move forward)
    def downForward(self):
        if (self.moveDownIsValid(self.point)):
            self.setPoint([self.point[0], self.point[1] + 1])
        while True:
            if (self.moveForwardIsValid(self.point)):
                return True
            if (not self.moveDownIsValid(self.point)):
                return self.backDown()
            self.setPoint([self.point[0], self.point[1] + 1])

    def backDown(self):
        if (self.moveBackwardIsValid(self.point)):
            self.setPoint([self.point[0] - 1, self.point[1]])
        while True:
            if (self.moveDownIsValid(self.point)):
                return self.downForward()
            if (not self.moveBackwardIsValid(self.point)):
                return self.upBack()
            self.setPoint([self.point[0] - 1, self.point[1]])

    def upBack(self):
        if (self.moveUpIsValid(self.point)):
            self.setPoint([self.point[0], self.point[1] - 1])
        while True:
            if (self.moveBackwardIsValid(self.point)):
                return self.backDown()
            if (not self.moveUpIsValid(self.point)):
                return False
            self.setPoint([self.point[0], self.point[1] - 1])

    def upForward(self):
        if (self.moveUpIsValid(self.point)):
            self.setPoint([self.point[0], self.point[1] - 1])
        while True:
            if (self.moveForwardIsValid(self.point)):
                return True
            if (not self.moveUpIsValid(self.point)):
                return self.backUp()
            self.setPoint([self.point[0], self.point[1] - 1])

    def backUp(self):
        if (self.moveBackwardIsValid(self.point)):
            self.setPoint([self.point[0] - 1, self.point[1]])
        while True:
            if (self.moveUpIsValid(self.point)):
                return self.upForward()
            if (not self.moveBackwardIsValid(self.point)):
                return self.downBack()
            self.setPoint([self.point[0] - 1, self.point[1]])

    def downBack(self):
        if (self.moveDownIsValid(self.point)):
            self.setPoint([self.point[0], self.point[1] + 1])
        while True:
            if (self.moveBackwardIsValid(self.point)):
                return self.backUp()
            if (not self.moveDownIsValid(self.point)):
                return False
            self.setPoint([self.point[0], self.point[1] + 1])

    def isValid(self, point): # this checks to see if a point is a valid move location (i have defined the field to be field[x][y] not field[y][x])
        for x in range(0, self.width):
            if (self.protectedCheckPoint(point[0] + x, point[1]) or self.protectedCheckPoint(point[0] + x, point[1] + self.width - 1) or self.protectedCheckPoint(point[0], point[1] + x) or self.protectedCheckPoint(point[0] + self.width - 1, point[1] + x)):
                return False;
        return True

    def protectedCheckPoint(self, x, y): # sees if a point has been taken
        if (y >= self.yMax or y < 0 or x < 0 or x >= self.xMax): # we will not allow points outside the zone to be valid
            return True;
        return self.field[x][y] # just check the point now

    def moveDownIsValid(self, point):  # checks below
        return self.isValid([point[0], point[1] + 1])

    def moveUpIsValid(self, point): #checks above
        return self.isValid([point[0], point[1] - 1])

    def moveForwardIsValid(self, point): #checks foreward
        self.message = "isValid = {}, point: ( {}, {} )".format(self.isValid([point[0] + 1, point[1]]), point[0], point[1])
        return self.isValid([point[0] + 1, point[1]])

    def moveBackwardIsValid(self, point): # checks backward 
        return self.isValid([point[0] - 1, point[1]])

    def printField(self, field):
        for y in range(0, 72):
            for x in range(0, 94):
                if (field[x][y]):
                    print(' x', end ="")
                else:
                    print('  ', end ="")
                # print(field[x][y], end = "")

    def setPoint(self, point): # a useful function for debuggin, but in normal function just sets a point
        self.point = [point[0], point[1]]
        if (self.debug): # if debugging print out the field
            print('\n\n\n\n\n\n\n\n\n\n\n\n')
            print(self.point)
            for y in range(0, self.yMax):
                print("")
                for x in range(0, self.xMax):
                    if (x >= point[0] and x <= point[0] + 23 and y >= point[1] and y <= point[1] + 23):
                        print(" *", end = "")
                    elif (self.field[x][y]):
                        print(" x", end = "")
                    else:
                        print("  ", end = "")
            print("\n{}".format(self.message))

            self.message = 'No Updates'
            sleep(self.sleep)
            print(self.message, end = '')

    def createDummyField(self): # a testing dummy field
        field = [[0 for i in range(72)] for j in range(94)]
        for x in range(0, len(field)):
            for y in range(0, len(field[0])):
                if (x == 67 or y == 535):
                    field[x][y] = 1
                else:
                    field[x][y] = 0
        return field

    def isComplete(self, point):
        if (self.point[0] == self.xMax - 24 and self.isValid(self.point)): # defines when the box reaxches the intended target and is valid
            return True
        return False
