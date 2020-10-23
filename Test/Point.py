class Point:
    def __init__(self, xVal, yVal):
        self.xVal_ = xVal
        self.yVal_ = yVal

    # Define the ability to multiply scalar by point
    def __mul__(self, other):
        return Point(other*self.xVal_, other*self.yVal_)

    def ToString(self):
        print("X:", self.xVal_, "Y:", self.yVal_)