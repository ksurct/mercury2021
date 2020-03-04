from pynput import keyboard
import os

motorSpeed = 50
lockySpeed = 5

rightForward = 'i'
leftForward = 'w'
rightBackward = 'k'
leftBackward = 's'
lockerUp = 'y'
lockerDown = 'h'

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        if (key.char == rightForward):
            print("Move right forward")
        elif (key.char == rightBackward):
            print("Move right backward")
        elif (key.char == leftForward):
            print("Move left forward")
        elif (key.char == leftBackward):
            print("Move left backward")
        elif (key.char == lockerUp):
            print("Move locker up")
        elif (key.char == lockerDown):
            print("Move locker down")
        else:
            print("Other key pressed")
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    print('{0} released'.format(key))
    print("STOP ALL MOVEMENT")
    if key == keyboard.Key.esc:
        # Stop listener
        return False

try:
    # Collect events until released
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except KeyboardInterrupt:
    print("Exiting program")

