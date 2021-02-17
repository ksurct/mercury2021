print("Running as actual robot")
# import mercury.controls.keyboard_drive    #Gets the probable theta
#     def getProbableTheta(self):
#         pass
from mercury.robot_control.real_robot_control import RealRobotControl


r = RealRobotControl()

r.setAllMotorSpeeds(50)