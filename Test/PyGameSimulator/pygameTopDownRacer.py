import pygame

# Stopped here https://youtu.be/dX57H9qecCU?list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO&t=88

pygame.init()

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

def car(x,y):
    gameDisplay.blit(carImg, (x,y)) # Blit draws the car


def game_loop():
    # Initial car starting position
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

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
        car(x,y) # Draw car after fill, Isaiah you dummy. 

        # Logic loop to check for things like collisions
        if x > display_width - car_width or x < 0:
            gameExit = True


        pygame.display.update() # or pygame.display.flip(). Updates the frame. 
        
        clock.tick(fps) # This argument is the frames per second

game_loop()
pygame.quit()
# Can run other quitting functions here if we need
quit()