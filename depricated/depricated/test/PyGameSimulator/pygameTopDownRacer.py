import pygame
import time
import random


pygame.init() # start the whole thing

# Vars
display_width  = 800
display_height = 600
title = 'Robo-Sim'
fps = 120
car_width = 37

# Colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)


gameDisplay = pygame.display.set_mode((display_width, display_height)) # This is essentially width and height of a game
pygame.display.set_caption(title)
clock = pygame.time.Clock() # Our game clock

carImg = pygame.image.load('SimpleOppy.png') # TODO use gimp to make this transparent

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh]) # use this to draw rectanges

def car(x,y):
    gameDisplay.blit(carImg, (x,y)) # Blit draws the car

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115) # second arg is font size
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)
    game_loop()

def crash():
    message_display('You crashed!')


def game_loop():
    # Initial car starting position
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    gameExit = False # Reset on car crashes

    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            


            print(event)
        x += x_change # apply change to our car

        gameDisplay.fill(white)

        # draw boxes
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed

        car(x,y) # Draw car after fill, Isaiah you dummy. 

        # Logic loop to check for things like collisions
        if x > display_width - car_width or x < 0:
            crash()
        
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)

        if y < thing_starty + thing_height:
            print("y crossover")

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print("x crossover")
                crash()        

        pygame.display.update() # or pygame.display.flip(). Updates the frame. 
        
        clock.tick(fps) # This argument is the frames per second

game_loop()
pygame.quit()
# Can run other quitting functions here if we need
quit()