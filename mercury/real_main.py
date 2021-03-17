import re
print("Running as actual robot")
# import mercury.controls.keyboard_drive    #Gets the probable theta
#     def getProbableTheta(self):
#         pass
from mercury.robot_control.real_robot_control import RealRobotControl
from mercury.internet_com import InternetCom
from time import sleep
com = InternetCom("robot", "http://10.150.251.154:8000/server")
r = RealRobotControl()
r.setClawServo(100)

while(True):
    com.send("computer")
    sleep(0.5)
