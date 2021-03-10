import re
print("Running as actual robot")
# import mercury.controls.keyboard_drive    #Gets the probable theta
#     def getProbableTheta(self):
#         pass
# from mercury.robot_control.real_robot_control import RealRobotControl
from mercury.Webserver_Compter import webserver

w = webserver()

r = RealRobotControl()
r.setServoAngle(100)
import time
#r.setAllMotorSpeeds(50)
print("Run")
while(True):
    pass
    command = w.send("robot somehow")
    command.pop(0)
    command = "".join(command)
    command = command[:-1]
    print("Running " + command) 
    # r.runCommand(command)
    w.send("computer")
    time.sleep(5)
    pass
