import pygame
import time
import random
from ObstacleField import ObstacleField

# Functions
#def DrawObstacleField(field : ObstacleField):

# def LoadAlgorithmList():

# def LoadObstacleFieldList():

# def LoadRobotKinematicModel():

def rot_center(image, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

# def rot_center(image, rect, angle):
#     """rotate an image while keeping its center"""
#     rot_image = pygame.transform.rotate(image, angle)
#     rot_rect = rot_image.get_rect(center=rect.center)
#     return rot_image,rot_rect



# Startup stuff here
pygame.init() # start the whole thing

# Vars
display_width  = 800
display_height = 600
title = 'Robo-Sim'
fps = 2

# Colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

# Init Block here
gameDisplay = pygame.display.set_mode((display_width, display_height)) # This is essentially width and height of a game
pygame.display.set_caption(title)
clock = pygame.time.Clock() # Our game clock
carImg = pygame.image.load('./PyGameSimulator/SimpleOppy.png') # TODO use gimp to make this transparent
#carRect = carImg.get_rect()

carRect = pygame.Rect(50, 50, 20, 20)# TODO create new rect here
# TODO checkout how to rotate this later

#carSurf = pygame.Surface((50, 50))
#carSurf.fill(green)
carSurf = pygame.image.load('./PyGameSimulator/VectorOppy.png')
carSurf = pygame.transform.scale(carSurf, (9*10, 11*10))





gameDisplay.fill(white)
pygame.display.update()

def game_loop(carImg, carRect, carSurf):

    # Loop variables
    # forwardBackwardVar = 0

    # robotX = (display_width * 0.45)
    # robotY = (display_height * 0.8)
    robotX = 150
    robotY = 150
    robotTheta = 0

    gameExit = False # Reset on car crashes

    while not gameExit:

        # Game event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # TODO Rotate thing ccw
                    print("Not yet implemented")
                elif event.key == pygame.K_RIGHT:
                    # TODO Rotate thing cw
                    print("Not yet implemented")
                elif event.key == pygame.K_UP:
                    forwardBackwardVar += 5
                elif event.key == pygame.K_UP:
                    forwardBackwardVar += -5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    # TODO clear out whatever we do here
                    forwardBackwardVar = 0

        
        # self.image=pygame.transform.rotate(self.saved_image, self.angle)
        # self.rect = self.image.get_rect(center=self.rect.center)
        # self.angle+=10

        # carImg = pygame.transform.rotate(carImg, robotTheta)
        # carImg = carImg.get_rect(center = carImg.center)
        # robotTheta += 10

        # carImg = rot_center(carImg, robotTheta)
        # robotTheta += 10

        # (carImg, carRect) = rot_center(carImg, carRect, robotTheta)
        # robotTheta += 10

        
        # Logic loop, check for things like collisions



        gameDisplay.fill(white)
        #gameDisplay.blit(carImg, (robotX,robotY)) # Blit draws the car

        # robotX += 1 
        # robotY += 1
        # print(robotX, robotY)
        # carRect = carRect.move(robotX, robotY)

        # robotX += 1 
        # robotY += 1
        robotTheta += 15
        print(robotTheta)
        carSurf = rot_center(carSurf, robotTheta)
        gameDisplay.blit(carSurf, (robotX, robotY))



        # pygame.draw.rect(gameDisplay, black, carRect)
        pygame.display.update()
        clock.tick(fps)
        # End while not gameExit

# The core game loop, if we exit this we exit the game.
game_loop(carImg, carRect, carSurf)
pygame.quit()
quit()