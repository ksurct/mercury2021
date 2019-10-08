from time import sleep
class PathFinder(object):
    """docstring for PathFinder."""

    def __init__(self):
        self.point = False # its false not a point
        self.width = 24
        self.debug = True

    def setField(self, field):
        self.field = field
        self.xMax = len(self.field) - 1
        self.yMax = len(self.field[0]) - 1

    def findStart(self):
        for x in range(0, len(self.field[0])):
            if self.isValid([0,x]):
                return [0,x]
        return False

    def checkField(self):
        self.point = self.findStart()
        if (not self.point):
            print('no point found')
            return False # it didnt even find a findStart
        # do the 'algo rythem' now
        self.setPoint(self.point)
        return self.moveForeward()

    def moveForeward(self):
        print('check field')
        stack = [];
        while True:

            if (not self.moveForwardIsValid(self.point)):
                curPoint = self.point
                stack.append(self.point)
                overideDown = False
                if (not overideDown and not self.downForward()):
                    self.point = stack.pop() # get the last valid foreward value
                    if (not self.upForward() and len(stack) == 0):
                        return False
                    elif (len(stack) > 0):
                        self.point = stack.pop() # if can't move up foreward and we have a stack make the self.point equal the last valid foreward point
                        overideDown = True # the only reason we
                else:
                    if (not self.upForward() and len(stack) == 0):
                        return False
                    elif (len(sFalsetack) > 0):
                        self.point = stack.pop()
                    overideDown = False
            self.setPoint([self.point[0] + 1, self.point[1]]) # just keep going
            if (self.isComplete(self.point)):
                return True

    def downForward(self):
        while True:
            if (self.moveForwardIsValid(self.point)):
                return True
            if (not self.moveDownIsValid(self.point)):
                return self.backDown()
            self.setPoint([self.point[0], self.point[1] + 1])

    def backDown(self):
        while True:
            if (self.moveDownIsValid(self.point)):
                return self.downForward()
            if (not self.moveBackwardIsValid(self.point)):
                return self.upBack()
            self.setPoint([self.point[0] - 1, self.point[1]])

    def upBack(self):
        while True:
            if (not self.moveUpIsValid(self.point)):
                return False
            if (self.moveBackwardIsValid(self.point)):
                return self.backDown()
            self.setPoint([self.point[0], self.point[1] - 1])

    def upForward(self):
        while True:
            if (self.moveForwardIsValid(self.point)):
                return True
            if (not self.moveUpIsValid(self.point)):
                return self.backUp()
            self.setPoint([self.point[0], self.point[1] - 1])

    def backUp(self):
        while True:
            if (self.moveUpIsValid(self.point)):
                return self.upForward()
            if (not self.moveBackwardIsValid(self.point)):
                return self.downBack()
            self.setPoint([self.point[0] - 1, self.point[1]])

    def downBack(self):
        while True:
            if (self.moveBackwardIsValid(self.point)):
                return backUp()
            if (not self.moveDownIsValid(self.point)):
                return False
            self.setPoint([self.point[0], self.point[1] + 1])
    """
    Might need to implement forwardUp and forwardDown
    """



    def isValid(self, point): # i have defined the field to be field[x][y] not field[y][x]
        for x in range(0, self.width):
            if (self.protectedCheckPoint(point[0] + x, point[1]) or self.protectedCheckPoint(point[0] + x, point[1] + self.width - 1) or self.protectedCheckPoint(point[0], point[1] + x) or self.protectedCheckPoint(point[0] + self.width - 1, point[1] + x)):
                return False;
        return True

    def protectedCheckPoint(self, x, y):
        if (y > self.yMax or y < 0 or x < 0 or x > self.xMax): # we will not allow points outside the y zone to be valid
            return True;
        return self.field[x][y] # just check the point now

    def moveDownIsValid(self, point):
        return self.isValid([point[0], point[1] + 1])

    def moveUpIsValid(self, point):
        return self.isValid([point[0], point[1] - 1])

    def moveForwardIsValid(self, point):
        return self.isValid([point[0] + 1, point[1]])

    def moveBackwardIsValid(self, point):
        return self.isValid([point[0] - 1, point[1]])

    def printField(self, field):
        for y in range(0, 72):
            for x in range(0, 94):
                if (field[x][y]):
                    print(' x', end ="")
                else:
                    print(' 0', end ="")
                # print(field[x][y], end = "")

    def setPoint(self, point):
        self.point = [point[0], point[1]]
        if (self.debug):
            print('\n\n\n\n\n\n\n')
            print(self.point)
            for y in range(0, self.yMax):
                print("")
                for x in range(0, self.xMax):
                    if (x >= point[0] and x <= point[0] + 23 and y >= point[1] and y <= point[1] + 23):
                        print(" *", end = "")
                    elif (self.field[x][y]):
                        print(" x", end = "")
                    else:
                        print(" 0", end = "")
            sleep(0.01)
    def createDummyField(self):
        field = [[0 for i in range(72)] for j in range(94)]
        for x in range(0, len(field)):
            for y in range(0, len(field[0])):
                if (x == 673 or y == 536):
                    field[x][y] = 1
                else:
                    field[x][y] = 0
        return field

    def isComplete(self, point):
        if (self.point[0] == self.xMax - 24):
            return True
        return False

#finder = PathFinder()
#finder.setField(finder.createDummyField())
# print(finder.protectedCheckPoint(-1, 0))
#print(finder.checkField())
