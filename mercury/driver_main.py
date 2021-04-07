print("Running as Driver")
from mercury.robot_control.robot_control import RobotControl
from mercury.internet_com import InternetCom
import pyglet
import pylint

w = InternetCom("computer", "http://10.150.251.154:8000/server")

window = pyglet.window.Window(width = 500, height = 500)
@window.event
def on_draw():
    window.clear()
    measures = sensors()
    sensor1 = pyglet.text.Label("Work in Progress", 
                          font_name ='Cooper', 
                          font_size = 16, 
                          x = 100,  
                          y = 100, 
                          anchor_x ='center',  
                          anchor_y ='center')
    #sensor2 = pyglet.text.Label("")
    sensor1.draw()

@window.event
def on_key_press(key, mod):
    keyP = chr(key)
    instruction = ""
    if(keyP == 'm'):
        instruction = r.createCommandInstruction(chr(key))
        #w.send(instruction)
        pyglet.app.exit()
    else:
        instruction = r.createCommandInstruction(keyP)
        #w.send(instruction)

r = RobotControl()
pyglet.app.run()