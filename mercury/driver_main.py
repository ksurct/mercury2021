print("Running as Driver")
from mercury.robot_control.robot_control import RobotControl
from mercury.internet_com import InternetCom
import pyglet
import pylint

w = InternetCom("computer", "http://10.150.251.154:8000/server")

window = pyglet.window.Window(width = 1000, height = 1000)

def redraw(self):
    count = 0
    count = count + 1
    window.clear()
    label = pyglet.text.Label(str(count), 
                          font_name ='Cooper', 
                          font_size = 16, 
                          x = 250,  
                          y = 150, 
                          anchor_x ='center',  
                          anchor_y ='center')
    label.draw()

pyglet.clock.schedule_interval(redraw, 0.5)
 
label = pyglet.text.Label("Hello World", 
                          font_name ='Cooper', 
                          font_size = 16, 
                          x = 250,  
                          y = 150, 
                          anchor_x ='center',  
                          anchor_y ='center')
   

# on draw event
@window.event
def on_draw():
    # clear the window
    window.clear()
    # draw the batch
    label.draw()


@window.event
def on_key_press(key, mod):
    global speed
    keyP = chr(key)
    instruction = ""
    if(keyP == 'm'):
        instruction = r.createCommandInstruction(keyP)
        #w.send(instruction)
        pyglet.app.exit()
    else:
        instruction = r.createCommandInstruction(keyP)
        #w.send(instruction)

r = RobotControl()
pyglet.app.run()