from pynput import keyboard
import pyglet
from mercury.motors.motor import motor
M1 = motor(18, 20)
M2 = motor(12, 21)
M3 = motor(13, 5)
M4 = motor(19, 6)

motors = [M1, M2, M3, M4]

window = pyglet.window.Window(width=10, height=10)
@window.event
def on_key_press(key, mod):
    key = chr(key)
    print("Pressed", key)

    if (key == "w"):
        for mot in motors:
            mot.setDirection(1)
            mot.setSpeed(50)
    elif (key == "s"):
        for mot in motors:
            mot.setDirection(-1)
            mot.setSpeed(50)
    elif (key == "d"):
        for mot in motors:
            mot.setSpeed(50)
        motors[0].setDirection(1)
        motors[1].setDirection(1)
        motors[2].setDirection(-1)
        motors[3].setDirection(-1)
    elif (key == "a"):
        for mot in motors:
            mot.setSpeed(50)
        motors[0].setDirection(-1)
        motors[1].setDirection(-1)
        motors[2].setDirection(1)
        motors[3].setDirection(1)
    elif (key == "q"):
        for mot in motors:
            mot.setSpeed(0)

def rel(key):
    print("Something released")
    
#listener = keyboard.Listener(onpress=on_press, onrelease=rel)
#with keyboard.Listener(onpress=on_press, onrelease=rel) as l:
#    l.join()
pyglet.app.run()
listener.start()
import time
while (True):
    print("Hello")
    time.sleep(1)