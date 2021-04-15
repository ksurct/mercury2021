print("Running as Driver")
from mercury.robot_control.robot_control import RobotControl
from mercury.internet_com import InternetCom
#from mercury.driver_interface_main import CreateSensors
import pyglet
import pylint

w = InternetCom("computer", "http://10.150.251.154:8000/server")


window = pyglet.window.Window(width = 500, height = 500)

labels = [pyglet.text.Label(text = "Frt L"), pyglet.text.Label(text = "Frt M"), 
    pyglet.text.Label(text = "Frt R"), pyglet.text.Label(text = "Left Frt"), 
    pyglet.text.Label(text = "Left Bk"), pyglet.text.Label(text = "Right Frt"), 
    pyglet.text.Label(text = "Right Bk")]
count = 7
for s in labels: 
    s.font_name = "Times New Roman"
    s.font_size = 35
    s.x = window.width//4
    s.y = (window.height//8 * count)
    s.anchor_x = "center"
    s.anchor_y = "center"
    count = count - 1

sensors = [pyglet.text.Label(), pyglet.text.Label(), pyglet.text.Label(), 
    pyglet.text.Label(), pyglet.text.Label(), 
    pyglet.text.Label(), pyglet.text.Label()]
count = 7
for s in sensors: 
    s.text = "sensor"
    s.font_name = "Times New Roman"
    s.font_size = 35
    s.x = window.width//4 * 3
    s.y = (window.height//8 * count)
    s.anchor_x = "center"
    s.anchor_y = "center"
    count = count - 1

@window.event
def on_draw():
    window.clear()
    for x in labels:
        x.draw()
    for s in sensors:
        s.draw()
        

@window.event
def on_key_press(key, mod):
    keyP = chr(key)
    instruction = ""
    if(keyP == 'm'):
        instruction = r.createCommandInstruction(chr(key))
        #response = w.send(instruction)
        pyglet.app.exit()
    else:
        instruction = r.createCommandInstruction(keyP)
        #response = w.send(instruction)
        for s in sensors:
            s.text = keyP

r = RobotControl()
pyglet.app.run()