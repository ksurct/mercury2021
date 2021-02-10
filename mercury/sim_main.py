print("Running as simulation")
from mercury.robot_control.sim_robot_control import SimRobotControl
import pyglet
# simple temp demonstration of simulated robot moving

r = None
PI = 3.14
def callback(test):
    print(test)
    r.move(10, 0);    
    r.rotate(0, 0)
r = SimRobotControl(callback, 0.1, 0.01)

pyglet.app.run()

