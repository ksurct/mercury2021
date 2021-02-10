# Write anything in this to test your code.
from mercury.time.time_keeper import TimeKeeper
from time import sleep
from mercury.robot_control.real_robot_control import RealRobotControl

r = RealRobotControl()

r.setAllMotorSpeeds(100)

r.move(1, 0.25)
