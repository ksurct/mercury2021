'''
    Basestation code for the robot
'''

from xbox import Controller
from networking import BasestationNetwork

def mainLoop():
    Controller.init()
    controller = Controller(0)
    network = BasestationNetwork('http://localhost:8000/')
    controllerDict = {}
    try:
        while True:
            controller.update()
            controllerDict['a'] = 1 if controller.a() else 0
            controllerDict['b'] = 1 if controller.b() else 0
            controllerDict['x'] = 1 if controller.x() else 0
            controllerDict['y'] = 1 if controller.y() else 0
            controllerDict['st'] = 1 if controller.select_button() else 0 #this is switched in xbox file
            controllerDict['se'] = 1 if controller.start_button() else 0
            controllerDict['rt'] = int(controller.right_trigger() >> 3) + 4096 #adding 4096 starts the trigger at 0
            controllerDict['lt'] = int(controller.left_trigger() >> 3) + 4096 #adding 4096 starts the trigger at 0
            controllerDict['rb'] = 1 if controller.right_bumper() else 0
            controllerDict['lb'] = 1 if controller.left_bumper() else 0
            r_stick_x = round(controller.right_x(), 1)
            r_stick_y = round(controller.right_y(), 1)
            l_stick_x = round(controller.left_x(), 1)
            l_stick_y = round(controller.left_y(), 1)
            controllerDict['rsx'] = int(10*r_stick_x) if abs(r_stick_x) > 0.1 else 0
            controllerDict['rsy'] = int(-10*r_stick_y) if abs(r_stick_y) > 0.1 else 0
            controllerDict['lsx'] = int(10*l_stick_x) if abs(l_stick_x) > 0.1 else 0
            controllerDict['lsy'] = int(-10*l_stick_y) if abs(l_stick_y) > 0.1 else 0
            controllerDict['u'] = 1 if str(controller.hat).strip() == 'u' else 0
            controllerDict['d'] = 1 if str(controller.hat).strip() == 'd' else 0
            controllerDict['l'] = 1 if str(controller.hat).strip() == 'l' else 0
            controllerDict['r'] = 1 if str(controller.hat).strip() == 'r' else 0
            network.sendController(controllerDict)
    except KeyboardInterrupt:
        print("Keyboard interrupt detected")
    finally:
        print("End of basestation main loop")

if __name__ == '__main__':
    print("Starting main loop...")
    mainLoop()