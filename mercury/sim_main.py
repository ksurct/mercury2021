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
def forwardRightLeftBack(test):
        #print(test)
        #time.sleep(.25)
        thetaTurn = 1.58

        empty = False
        r.rotate(0, 0)
        x = r.getSensorData()
        highRight = x[0]
        highLeft = x[1]
        lowLeft = x[2]
        lowRight = x[3]
        frontRight = x[4]
        frontLeft = x[5]
        frontMid = x[6]

        #print out what the sensors are detecting for testing purposes
        measures = str(highRight[0]) + highRight[1] + "   " + str(lowRight[0]) + lowRight[1]+ "   " + str(highLeft[0]) + highLeft[1] + "   " + str(lowLeft[0]) + lowLeft[1] + "   " + str(frontRight[0]) + frontRight[1] + "   " + str(frontMid[0]) + frontMid[1] + "   " + str(frontLeft[0]) + frontLeft[1]
        #print(measures)
        
        #If nothing is detected in front of the robot
        if (frontRight[0] == empty and frontLeft[0] == empty and frontMid[0] == empty):
            
            print("forward")
            r.move(10,0)
            print(r.getProbableTheta())
        #something is in front a front facing sensors
        else: 
            t = (r.getProbableTheta() / 6.29) % 1
            print("TurnTheta" + str(t))
            #theta for from right to facing south is between 3.14 and 4.71, if it turns left, theta is reduced
            if (t >= 0.25 and t < .5):
                #if something is to the right, see if you can rotate left
                if (highLeft[0] == empty and lowLeft[0] == empty):
                    print("left")
                    r.rotate(-PI/2,0)
                    print("TurnTheta" + str(t))
                    print(r.getProbableTheta())
                elif (highRight[0] == empty and lowRight[0] == empty):
                    print("right")
                    r.rotate(PI/2, 0)
                    print("TurnTheta" + str(t))
                    print(r.getProbableTheta())
                #if there is something to both right and left, go backwards and then try to rotate 
                else:
                    print("reverse")
                    r.rotate(PI, 0)
                    print("TurnTheta" + str(t))
                    print(r.getProbableTheta())
            
            else:
                if (highRight[0] == empty and lowRight[0] == empty):
                    print("right")
                    r.rotate(PI/2, 0)
                    print("TurnTheta" + str(t))
                    print(r.getProbableTheta())
                #if something is to the right, see if you can rotate left
                elif (highLeft[0] == empty and lowLeft[0] == empty):
                    print("left")
                    r.rotate(-PI/2,0)
                    print("TurnTheta" + str(t))
                    print(r.getProbableTheta())
                #if there is something to both right and left, go backwards and then try to rotate 
                else:
                    print("reverse")
                    r.rotate(PI, 0)
                    print("TurnTheta" + str(t))
                    print(r.getProbableTheta())
            

r = SimRobotControl(forwardRightLeftBack, 0.1, 0.00)

pyglet.app.run()

