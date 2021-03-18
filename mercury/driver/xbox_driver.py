import signal
from xbox360controller import Xbox360Controller
from time import sleep
import time, threading

from mercury.internet_com import InternetCom
class XboxDriver():
    def __init__(self):
        self.rightSpeed = 0
        self.leftSpeed = 0
        self.servoAngle = 0
        self.armAngle = 90
        self.clawAngle = 90
        self.command = ""
        self.controller = None
        self.com = InternetCom("computer")

    def on_button_pressed(self,button):
        print('Button {0} was pressed'.format(button.name))

    def on_button_released(self,button):
        print('Button {0} was released'.format(button.name))

    def on_axis_moved(self,axis):
        if (axis.name == "axis_r"):
            self.rightSpeed = -50 * axis.y

    def createCommandString(self, ls, rs, aa, ca):
        ##example: string = CONTINUOUS,  100, 49, 180, 90
        if (abs(ls) < 0.1):
            ls = 0
        if (abs(rs) < 0.1):
            rs = 0
        self.command = "CONTINUOUS, {}, {}, {}, {}".format(ls*-100,rs*-100,aa,ca)
        return self.command
    def signal(self):
        try:
            with Xbox360Controller(0, axis_threshold=0.2) as controller:
                # Button A events
                self.controller = controller
                print("INIT: ", controller.axis_r._value_y)
                controller.button_a.when_pressed = self.on_button_pressed
                controller.button_a.when_released = self.on_button_released
                controller.button_b.when_pressed = self.on_button_pressed
                controller.button_b.when_released = self.on_button_released
                controller.button_x.when_pressed = self.on_button_pressed
                controller.button_x.when_released = self.on_button_released
                controller.button_y.when_pressed = self.on_button_pressed
                controller.button_y.when_released = self.on_button_released
                controller.button_trigger_l.when_released = self.on_button_released
                controller.button_trigger_l.when_pressed = self.on_button_pressed
                controller.button_trigger_r.when_pressed = self.on_button_pressed
                controller.button_trigger_r.when_released = self.on_button_released
                controller.button_thumb_l.when_released = self.on_button_released
                controller.button_thumb_l.when_pressed = self.on_button_pressed
                controller.button_thumb_r.when_released = self.on_button_released
                controller.button_thumb_r.when_pressed = self.on_button_pressed

                # Left and right axis move event
                controller.axis_l.when_moved = self.on_axis_moved
                controller.axis_r.when_moved = self.on_axis_moved
                signal.pause()
        except KeyboardInterrupt:
            pass

    def run(self):
        threading.Timer(1, self.run).start()
        print("Sending: {}".format(self.createCommandString(self.controller.axis_l._value_y, self.controller.axis_r._value_y, 90, 90)))
        if (self.controller != None):
            print("INIT: ", self.controller.axis_r._value_y)
        self.com.send(self.command)
if (__name__ == "__main__"):
    import time, threading
    x = XboxDriver()
    print(time.ctime())
    threading.Timer(0.5, x.run).start()
    x.signal()