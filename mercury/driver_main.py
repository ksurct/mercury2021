print("Running as Driver")
from mercury.robot_control.robot_control import RobotControl
from mercury.internet_com import InternetCom
#from mercury.driver_interface_main import CreateSensors
import pyglet
import pylint

w = InternetCom("computer", "http://10.150.251.154:8000/server")


window = pyglet.window.Window(width = 500, height = 500)

"""
#code in progress to streamline the label creation for sensors
sensorsFL = pyglet.text.Label
sensorsFM = pyglet.text.Label
sensorsFR = pyglet.text.Label
sensorsLT = pyglet.text.Label
sensorsLB = pyglet.text.Label
sensorsRT = pyglet.text.Label
sensorsRB = pyglet.text.Label
sensors = [sensorsFL, sensorsFM, sensorsFR, sensorsLT, sensorsLB, sensorsRT, sensorsRB]

for s in sensors:
    count = 7 
    s = pyglet.text.Label('Sensor',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//4, y=window.height//8 * count,
                          anchor_x='center', anchor_y='center')
    count = count - 1"""
#first iteration of working changing text for interface
sensorsFL = pyglet.text.Label('Front Left',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//8 * 7,
                          anchor_x='center', anchor_y='center')
sensorsFM = pyglet.text.Label('Front middle',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//8 * 6,
                          anchor_x='center', anchor_y='center')
sensorsFR = pyglet.text.Label('Front right',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//8 * 5,
                          anchor_x='center', anchor_y='center')
sensorsLT = pyglet.text.Label('Left top',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//8 * 4,
                          anchor_x='center', anchor_y='center')
sensorsLB = pyglet.text.Label('Left bottom',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//8 * 3,
                          anchor_x='center', anchor_y='center')
sensorsRT = pyglet.text.Label('Right top',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//8 * 2,
                          anchor_x='center', anchor_y='center')
sensorsRB = pyglet.text.Label('Right bottom',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//8,
                          anchor_x='center', anchor_y='center')
                          
sensors = [sensorsFL, sensorsFM, sensorsFR, sensorsLT, sensorsLB, sensorsRT, sensorsRB]

@window.event
def on_draw():
    window.clear()
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