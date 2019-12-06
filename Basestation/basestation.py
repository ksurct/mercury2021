'''
    Basestation code for the robot
'''

from xbox import Controller
from networking import BasestationNetwork

def mainLoop():
    Controller.init()
    controller = Controller(0)
    network = BasestationNetwork('http://localhost:8000/')
    try:
        while True:
            controllerDict = getControllerData(controller)
            network.sendController(controllerDict)
    except KeyboardInterrupt:
        print("Keyboard interrupt detected")
    finally:
        print("End of basestation main loop")

def getControllerData(controller):
    controller.update()
    tempControlData = {}
    tempControlData['a'] = 1 if controller.a() else 0
    tempControlData['b'] = 1 if controller.b() else 0
    tempControlData['x'] = 1 if controller.x() else 0
    tempControlData['y'] = 1 if controller.y() else 0
    tempControlData['st'] = 1 if controller.select_button() else 0 #this is switched in xbox file
    tempControlData['se'] = 1 if controller.start_button() else 0
    tempControlData['rt'] = int(controller.right_trigger() >> 3) + 4096 #adding 4096 starts the trigger at 0
    tempControlData['lt'] = int(controller.left_trigger() >> 3) + 4096 #adding 4096 starts the trigger at 0
    tempControlData['rb'] = 1 if controller.right_bumper() else 0
    tempControlData['lb'] = 1 if controller.left_bumper() else 0
    r_stick_x = round(controller.right_x(), 1)
    r_stick_y = round(controller.right_y(), 1)
    l_stick_x = round(controller.left_x(), 1)
    l_stick_y = round(controller.left_y(), 1)
    tempControlData['rsx'] = int(10*r_stick_x) if abs(r_stick_x) > 0.1 else 0
    tempControlData['rsy'] = int(-10*r_stick_y) if abs(r_stick_y) > 0.1 else 0
    tempControlData['lsx'] = int(10*l_stick_x) if abs(l_stick_x) > 0.1 else 0
    tempControlData['lsy'] = int(-10*l_stick_y) if abs(l_stick_y) > 0.1 else 0
    tempControlData['u'] = 1 if str(controller.hat).strip() == 'u' else 0
    tempControlData['d'] = 1 if str(controller.hat).strip() == 'd' else 0
    tempControlData['l'] = 1 if str(controller.hat).strip() == 'l' else 0
    tempControlData['r'] = 1 if str(controller.hat).strip() == 'r' else 0
    return tempControlData


if __name__ == '__main__':
    print("Starting main loop...")
    mainLoop()