import keyboard

motorSpeed = 50
lockySpeed = 5

def leftMotorForward(event):
    pass

def rightMotorForward(event):
    pass

def leftMotorStop(event):
    pass

def rightMotorStop(event):
    pass

def leftMotorReverse(event):
    pass

def rightMotorReverse(event):
    pass

def lockyDown(event):
    pass

def lockyUp(event):
    pass

def lockyStop(event):
    pass

keyboard.on_press_key('w', leftMotorForward)
keyboard.on_press_key('u', rightMotorForward)
keyboard.on_press_key('s', leftMotorReverse)
keyboard.on_press_key('j', rightMotorReverse)
keyboard.on_release_key('w', leftMotorStop)
keyboard.on_release_key('u', rightMotorStop)
keyboard.on_release_key('s', leftMotorReverse)
keyboard.on_release_key('j', rightMotorStop)

keyboard.on_press_key('t', lockyDown)
keyboard.on_press_key('g', lockyUp)
keyboard.on_release_key('t', lockyStop)
keyboard.on_release_key('g', lockyStop)

try:
    while True:
        pass
except KeyboardInterrupt:
    keyboard.unhook_all()
    print("Everything unhooked")

