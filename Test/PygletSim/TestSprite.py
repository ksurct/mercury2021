import pyglet
from math import *
PI = 3.1415
class Visualizer():
    def __init__(self):
        self.img = pyglet.image.load('Arrow.png')
        self.img.anchor_x = self.img.width // 2 + 1
        self.img.anchor_y = self.img.height // 2 + 1
        self.main_batch = pyglet.graphics.Batch()

        self.robot = pyglet.sprite.Sprite(self.img, x=300, subpixel=True, y=300)

        self.window = pyglet.window.Window(width=600, height=600)
        # self.pixels = self.window.get
        # self.drawSquare(10, 10, 200, 200)
        self.PsuedoRayCast = PsuedoRayCast(self.window)
        self.boxes = None

    def setBoxes(self, boxes):
        self.boxes = boxes

    def drawSquare(self, a, b, c, d):
        # glClear(GL_COLOR_BUFFER_BIT)

        self.main_batch.add(8, pyglet.gl.GL_LINES, None,
                            ('v2f', (a, b, c, b, a,b,a,d, c,b,c,d, a,d,c,d),
                        ))
        self.main_batch.draw()

    def drawAllBoxes(self):
        if (not self.boxes):
            return
        for box in self.boxes:
                self.drawSquare(box[0][0], box[0][1], box[1][0], box[1][1])

    def redraw(self):
        print("redraw")
        self.window.clear()
        self.drawAllBoxes()
        for i in range(-300, 300):
            pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
            ('v2i', (self.robot.position[0] + i, self.robot.position[1])),
            ('c3B', (0, 0, 255))
            )
        for i in range(-300, 300):
            pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
            ('v2i', (self.robot.position[0], i + self.robot.position[1])),
            ('c3B', (0, 0, 255))
            )
        pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
            ('v2f', self.getFrontSensorPoint()),
            ('c3B', (0, 255, 0))
            )

    def setXYAbsolute(self, x, y):
        self.robot.position = (x, y)
        self.redraw()

    def setΘAbsolute(self, Θ):
        self.robot.rotation = Θ
        self.redraw()

    def setXYRelative(self, x, y):
        self.robot.position = (self.robot.position[0] + x, self.robot.position[1] + y)
        self.redraw()

    def setΘReltive(self, Θ):
        self.robot.rotation = self.robot.rotation + Θ
        self.redraw()

    def radToDeg(self, Θ):
        return (180 / PI) * Θ
    def degToRad(self, Θ):
        return (PI / 180) * Θ
    def getFrontSensorPoint(self):
        return (sin(self.degToRad(self.robot.rotation))*self.img.height // 2 + self.robot.position[0], cos(self.degToRad(self.robot.rotation))*self.robot.height // 2 + self.robot.position[1])
    def getFrontSensorData(self):
        return self.getFrontSensorPoint();


class PsuedoRayCast():
    def __init__(self, window): # takes in a pyglet window objectalison
        self.window = window
        print("cast the ray")

    def getLineFunction(self, a, b, Θ):
        return lambda x: (1/tan(Θ))(x - a) + b;
    def findObj(self, f, mod, a, b):
        limitX = self.window.width - a
        limitY = self.window.height - b
        for i in range(a, limitX):
            if (f(i) > limitY):
                break
            
    def checkPoint(self, a, b):
        print("")

vis = Visualizer()


@vis.window.event
def on_draw():
    vis.robot.draw()

@vis.window.event
def on_key_press(key, mod):
    print("point: ", vis.robot.position)
    key = chr(key)
    if (key == 'a'):
        vis.setXYRelative(-10, 0);
    if (key == 's'):
        vis.setXYRelative(0, -10)
    if (key == 'd'):
        vis.setXYRelative(10, 0)
    if (key == 'w'):
        vis.setXYRelative(0, 10)
    if (key == 'p'):
        vis.setΘReltive(15) 
    if (key == 'o'):
        vis.setΘReltive(-15) 
    print(vis.getFrontSensorData())
pyglet.app.run()