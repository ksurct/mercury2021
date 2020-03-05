from pynput import keyboard
import os
from HardwareModels import MotorModel
import settings as s

motorSpeed = 6
lockySpeed = 5

rightForward = 'i'
leftForward = 'w'
rightBackward = 'k'
leftBackward = 's'
lockerUp = 'y'
lockerDown = 'h'

flMotor = MotorModel(s.frontLeftInitDict)
frMotor = MotorModel(s.frontRightInitDict)
rlMotor = MotorModel(s.rearLeftInitDict)
rrMotor = MotorModel(s.rearRightInitDict)

def on_press(key):
    try:
        #print('alphanumeric key {0} pressed'.format(key.char))
        if (key.char == rightForward):
            #print("Move right forward")
            frMotor.move(motorSpeed)
            rrMotor.move(motorSpeed)
        elif (key.char == rightBackward):
            #print("Move right backward")
            frMotor.move(motorSpeed * -1)
            rrMotor.move(motorSpeed * -1)
        elif (key.char == leftForward):
            #print("Move left forward")
            flMotor.move(motorSpeed)
            rlMotor.move(motorSpeed)
        elif (key.char == leftBackward):
            #print("Move left backward")
            flMotor.move(motorSpeed * -1)
            rlMotor.move(motorSpeed * -1)
        elif (key.char == lockerUp):
            print("Move locker up")
        elif (key.char == lockerDown):
            print("Move locker down")
        else:
            print("Other key pressed")
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    #print('{0} released'.format(key))
    print("STOP ALL MOVEMENT")
    flMotor.move(0)
    rlMotor.move(0)
    frMotor.move(0)
    rrMotor.move(0)
    if key == keyboard.Key.esc:
        # Stop listener
        return False 

try:
    # Collect events until released
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except KeyboardInterrupt:
    print("Exiting program")

