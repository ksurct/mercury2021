
class PathFinder(object):
    """docstring for PathFinder."""

    def __init__(self, ObstacleField):
        self.field = ObstacleField # expects big array with all valid points 0 and not valid 1 or True False
        self.point = False # its false not a point
        self.xMax = 95
        self.yMax = 71
        self.width = 24

    def checkField():
        self.point = findStart()
        if (!self.point):
            return False # it didnt even find a findStart
        # do the 'algo rythem' now
        return moveForeward()

    def moveForeward(point):
        stack = [];
        stack.append(point)
        while len(stack) > 0:

            if (not moveForwardIsValid(self.point)):
                curPoint = self.point
                stack.append(self.point)
                overideDown = False
                if (not downForward() and not overideDown):
                    self.point = curPoint # get the last valid foreward value
                    if (not upForward() and len(stack) == 0):
                        return False
                    elif (len(stack) > 0):
                        self.point = stack.pop() # if can't move up foreward and we have a stack make the self.point equal the last valid foreward point
                        overideDown = True # the only reason we
                else:
                    if (not upForward() and len(stack) == 0):
                        return False
                    elif (len(stack) > 0):
                        self.point = stack.pop()
                    overideDown = False
            self.point = [self.point[0] + 1, self.point[1]] # just keep going
    def downForward():
        while True:
            if (moveForwardIsValid(self.point)):
                return True
            if (not moveDownIsValid(self.point)):
                return backDown(self.point)
        self.point = [self.point[0], self.point[1] + 1]

    def backDown():
        while True:
            if (not moveBackwardIsValid()):
                return upBack()
            if (moveDownIsValid()):
                return downForward()
            self.point = [self.point[0] - 1, self.point[1]]

    def upBack():
        while True:
            if (not moveUpIsValid(self.point)):
                return False
            if (moveBackwardIsValid()):
                return backDown()
            self.point = [self.point[0], self.point[1] - 1];

    def upForward():
        while True:
            if (moveForwardIsValid(self.point)):
                return True
            if (not moveUpIsValid(self.point)):
                return backUp()
        self.point = [self.point[0], self.point[1] - 1]

    def backUp():
        while True:
            if (moveUpIsValid(self.point)):
                return upForward()
            if (not moveBackwardIsValid(self.point)):
                return downBack()
            self.point = [self.point[0] - 1, self.point[1]]

    def downBack():
        while True:
            if (moveBackwardIsValid(self.point)):
                return backUp()
            if (not moveDownIsValid()):
                return False
            self.point = [self.point[0], self.point[1] - 1]



    def isValid(point): # i have defined the field to be field[x][y] not field[y][x]
        for x in range(0, self.width):
            if (protectedCheckPoint(point[0] + x, point[1]) or protectedCheckPoint(point[0] + x, point[1] + self.width) or protectedCheckPoint(point[0], point[1] + x) or protectedChecksPoint(point[0] + self.width, point[1] + x)):
                return False;

    def protectedCheckPoint(x, y):
        if (x > self.xMax: # we will allow points outside the x direction to be valid
            return True;
        else if (y > self.yMax or y < 0): # we will not allow points outside the y zone to be valid
            return False;
        return self.field[x][y]; # just check the point now

    def moveDownIsValid(point):
        return isValid([point[0], point[1] + 1])

    def moveUpIsValid(point):
        return isValid([point[0], point[1] - 1])

    def moveForwardIsValid(point):
        return isValid([point[0] + 1, point[1]])

    def moveBackwardIsValid(point):
        return isValid([point[0] - 1, point[1]])

    def findStart():
        for x in range(0, len(self.field[0])):
            if isValid(x, 0):
                return [x,0]
        return False
