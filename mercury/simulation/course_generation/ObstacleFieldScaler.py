from ObstacleField import ObstacleField
from Point import Point

# This class uses a scale factor to increase the size of an obstacle field
# Ex: ObstacleFieldScaler(10, field) will return a field 10x the size of the input
class ObstacleFieldScaler:
    def __init__(self, scale_factor : float, field : ObstacleField):

        # check the scale factor to make sure it's >=1
        if scale_factor < 1:
            raise ValueError("Scale factor must be >= 1.")

        scale_factor = float(scale_factor)
        if not (scale_factor).is_integer() :
            raise ValueError("Scale factor must be a whole number (not fraction)")
        scale_factor = int(scale_factor)

        self.scale_factor_ = scale_factor
        self.field_ = field

        # Scale the field that we just received by using the scale factor
        self.scaled_field_ = self.ScaleField()

    # def __init__(self, heightInches = 72, widthInches = 96, entranceWidth = 24, entranceOffset = 34, exitWidth = 24, exitOffset = 6, occupiedPoints = []):
    def ScaleField(self):
        sf = self.scale_factor_
        newHeight = sf*self.field_.heightInches_
        newWidth = sf*self.field_.widthInches_
        newentranceWidth = sf*self.field_.entranceWidth_
        newentranceOffset = sf*self.field_.entranceOffset_
        newexitWidth = sf*self.field_.exitWidth_
        newexitOffset = sf*self.field_.exitOffset_
        
        # Generate out new points
        newoccupiedPoints = []
        for point in self.field_.occupiedPoints_:
            newoccupiedPoints.extend(self.ScalePoint(point))

        return ObstacleField(newHeight, newWidth, newentranceWidth, newentranceOffset, newexitWidth, newexitOffset, newoccupiedPoints)

    def ScalePoint(self, p_org : Point):
        x_low = p_org.xVal_*self.scale_factor_ - (self.scale_factor_ - 1)
        x_high = p_org.xVal_*self.scale_factor_
        x_range = range(x_low, x_high+1)

        y_low = p_org.yVal_*self.scale_factor_ - (self.scale_factor_ - 1)
        y_high = p_org.yVal_*self.scale_factor_
        y_range = range(y_low, y_high+1)

        out = []
        for i in x_range:
            for j in y_range:
                out.append(Point(i,j))

        return out




    
if __name__ == "__main__":
    # testField = ObstacleField(72, 96, 24, 34, 24, 6, [Point(3,3), Point(3,4), Point(3,5), Point (3,6)])
    testField = ObstacleField(8, 10, 2, 2, 2, 2, [Point(3,3), Point(3,4), Point(3,5), Point (3,6)])
    scaler = ObstacleFieldScaler(4, testField)




    print("\nOriginal")
    print(scaler.field_.toString())
    print("\n\nScaled by:", scaler.scale_factor_)
    print("\n\nResult")
    print(scaler.scaled_field_.toString())
    
