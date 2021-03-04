print("Running as Driver")
from mercury.robot_control.robot_control import RobotControl

speed = 0
#String Template: "CONTINUOUS",{LEFT SPEED},{RIGHT SPEED},------------{ARM SERVO PWM},{CLAW SERVO PWM}
        #example: string = CONTINUOUS,  100, 49,

        #String Template: "DISCRETE", {"MOVE"/"ROTATE"}, {METERS/DEGREES}, {SPEED}
        #example: string = DISCRETE, MOVE, 0.5, 50
        #example: string = DISCRETE, ROTATE, 90, 50\
def CommandConstruction(key):
    movementCommand = ""
    speedCommand = ""
    if (key == "w"):
        speedCommand = "CONTINUOUS, " + str(speed) + ", " + str(speed)
        r.runCommand(speedCommand)
        movementCommand = "DISCRETE, MOVE, " + str(speed)
        r.runCommand(movementCommand)
    elif (key == "a"):
        speedCommand = "CONTINUOUS, " + str(speed/5) + ", " + str(speed)
        r.runCommand(speedCommand)
        movementCommand = "DISCRETE, ROTATE, 100, " + str(speed)
        r.runCommand(movementCommand)
    elif (key == "d"):
        speedCommand = "CONTINUOUS, " + str(speed) + ", " + str(speed/5)
        r.runCommand(speedCommand)
        movementCommand = "DISCRETE, ROTATE, 100, " + str(speed)
        r.runCommand(movementCommand)
    elif (key == "1"):
        speed = 10
    elif (key == "2"):
        speed = 20
    elif (key == "3"):
        speed = 30
    elif (key == "4"):
        speed = 40
    elif (key == "5"):
        speed = 50
    elif (key == "6"):
        speed = 60
    elif (key == "7"):
        speed = 70
    elif (key == "8"):
        speed = 80
    elif (key == "9"):
        speed = 90
    elif (key == "10"):
        speed = 100



    #r = SimRobotControl(callback, 0.1, 0)
r = RobotControl(CommandConstruction)