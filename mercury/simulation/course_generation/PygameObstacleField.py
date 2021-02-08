from ObstacleField import *
import pygame

# This class in intended to visualize and animate the obstacle field and robot. 
class PygameObstacleField:
    def __init__(self, robotModel, obstacleField : ObstacleField):

        # Grab the dimensions from the obstacle field this will be based on. 
        self.heightInches = obstacleField.heightInches
        self.widthInches = obstacleField.widthInches
        self.entranceWidth = obstacleField.entranceWidth
        self.entranceOffset = obstacleField.entranceOffset
        self.exitWidth = obstacleField.exitWidth
        self.exitOffset = obstacleField.exitOffset
        self.occupiedPoints = obstacleField.occupiedPoints

        self.tunnelWidth = 25 # make the enterance and exit tunnels 25 inches long
        totalWidth = self.widthInches + 2*self.tunnelWidth

        # pygame initialization and variables
        pygame.init()
        self.title = 'Robo Sim'
        self.fps = 60
        
        # Color defs in RGB
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (255,0,0)

        # Get our display, title and clocket setup. 
        self.gameDisplay = pygame.display.set_mode((totalWidth+2, self.heightInches+2)) # This is essentially width and height of a game
                                                                                   # The plus 2 allows for edge borders
        pygame.display.set_caption(title)
        clock = pygame.time.Clock() # Our game clock

        # Robot Sprite setup
        robotImg = pygame.image.load('\PyGameSimulator\SimpleOppy.png')
        self.robotLen = 24 # TODO get a more reasonable number
        self.robotWidth = 24 # TODO get a more reasonable number

    def loop(self):
        # Control Loop

        # Intermediate stuff
        gameDisplay.fill(white)

        # Logic Loop

        pygame.display.update()
        clock.tick(fps)

    
if __name__ == "__main__":
    # You can choose to only specify the points this way, and keep the default arguments
    testField = ObstacleField(occupiedPoints=[Point(3,3), Point(3,4)])

    loop()


        









    #def registerController():
    