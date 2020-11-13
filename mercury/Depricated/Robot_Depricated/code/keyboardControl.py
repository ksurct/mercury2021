try:
    from pynput import keyboard
    import os
    from HardwareModels import MotorDriverModel
    import settings as s

    motorSpeed = 6
    lockySpeed = 5

    rightForward = 'i'
    leftForward = 'w'
    rightBackward = 'k'
    leftBackward = 's'
    lockerUp = 'y'
    lockerDown = 'h'

    file = open("keyboards.txt", 'a')
    file.write("Test")
    file.close()

    rightBoard = MotorDriverModel([s.frontRightInitDict, s.rearRightInitDict], 'rsy')
    leftBoard = MotorDriverModel([s.frontLeftInitDict, s.rearLeftInitDict], 'lsy')

    def on_press(key):
        try:
            #print('alphanumeric key {0} pressed'.format(key.char))
            if (key.char == rightForward):
                #print("Move right forward")
                rightBoard.moveMotors(motorSpeed)
            elif (key.char == rightBackward):
                #print("Move right backward")
                rightBoard.moveMotors(motorSpeed * -1)
            elif (key.char == leftForward):
                #print("Move left forward")
                leftBoard.moveMotors(motorSpeed)
            elif (key.char == leftBackward):
                #print("Move left backward")
                leftBoard.moveMotors(motorSpeed * -1)
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
        rightBoard.moveMotors(0)
        leftBoard.moveMotors(0)
        if key == keyboard.Key.esc:
            # Stop listener
            return False 

    try:
        # Collect events until released
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("Exiting program")
except Exception as e:
    file = open("keyboards.txt", 'a')
    file.write(e)
    file.close()

