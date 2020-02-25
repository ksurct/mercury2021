# Sleepy, stopped at:
# Start by creating a game.player module,
# in https://pyglet.readthedocs.io/en/stable/programming_guide/examplegame.html

import pyglet

class PhysicalObject(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #self.velocity_x, self.velocity_y = 0.0, 0.0
        self.velocity_x, self.velocity_y = 1.0, 1.0

    def update(self, dt): 
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt


def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

def update(dt):
    "Updates all objects in game_objects"
    for obj in game_objects:
        obj.update(dt)

# Create a batch for drawing a bunch of objects at once
main_batch = pyglet.graphics.Batch()

window = pyglet.window.Window()
image = pyglet.resource.image('VectorOppy.png')
# Scale image to be seeable for debugging
image.height = 10*image.height
image.width = 10*image.width
center_image(image) # Always anchor your images after loading

# Create our sprite from image
robotSprite = PhysicalObject(img=image, x = 400, y = 300, batch = main_batch)

roboX = 50
roboY = 50
roboTheta = 0

game_objects = [robotSprite] # Add other objects here






@window.event
def on_key_press(symbol, modifiers):
    print('Key Press')
    if symbol == pyglet.window.key.A:
        print('A was pressed')
    elif symbol == pyglet.window.key.LEFT:
        print('Left was pressed')
    elif symbol == pyglet.window.key.RIGHT:
        print('Right was pressed')

@window.event
def on_draw():
    window.clear()
    #image.blit(roboX,roboY)
    main_batch.draw()

@window.event
def on_key_release(symbol, modifiers):
    print('Key Released')
    if symbol == pyglet.window.key.A:
        print('A was released')
    elif symbol == pyglet.window.key.LEFT:
        print('Left was released')
    elif symbol == pyglet.window.key.RIGHT:
        print('Right was released')


pyglet.clock.schedule_interval(update, 1/120.0) # calls the update() function 120Hz
pyglet.app.run()

