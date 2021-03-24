import re
print("Running as actual robot")
# import mercury.controls.keyboard_drive    #Gets the probable theta
#     def getProbableTheta(self):
#         pass
from mercury.robot_control.real_robot_control import RealRobotControl
from mercury.internet_com import InternetCom
from time import sleep
import time
com = InternetCom("robot", "http://10.150.251.154:8000/server")
r = RealRobotControl()
r.setClawServo(100)
time_since_last_command = time.time()

while(True):
    if(time.time() - time_since_last_command > 2):
        r.setAllMotorSpeeds(0)
    try:
        command = com.send("computer")
        if(command != ""):
            time_since_last_command = time.time()
        r.runCommand(command)
    except:
        print("We are experiencing technical difficulties.")
    sleep(0.25)
