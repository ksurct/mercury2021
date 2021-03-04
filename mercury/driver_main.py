print("Running as Driver")
from mercury.robot_control.robot_control import RobotControl
from mercury.Webserver_Compter import webserver

w = webserver()
#String Template: "CONTINUOUS",{LEFT SPEED},{RIGHT SPEED},------------{ARM SERVO PWM},{CLAW SERVO PWM}
        #example: string = CONTINUOUS,  100, 49,

        #String Template: "DISCRETE", {"MOVE"/"ROTATE"}, {METERS/DEGREES}, {SPEED}
        #example: string = DISCRETE, MOVE, 0.5, 50
        #example: string = DISCRETE, ROTATE, 90, 50\
def CommandConstruction(key, speed):
    movementCommand = ""
    speedCommand = ""
    if (not bool(speed)):
        speed = 100

    #forward
    if (key == "w"):
        if (speed > 0 and speed <= 100):
            speedCommand = "CONTINUOUS, " + str(int(speed)) + ", " + str(int(speed))
            w.send(speedCommand)
            #r.runCommand(speedCommand)
            movementCommand = "DISCRETE, MOVE, 100, " + str(int(speed))
            w.send(movementCommand)
            #r.runCommand(movementCommand)
    #left
    elif (key == "a"):
        if (speed > 0 and speed <= 100):
            speedCommand = "CONTINUOUS, " + str(int(speed*-1)) + ", " + str(int(speed))
            w.send(speedCommand)
            #r.runCommand(speedCommand)
            movementCommand = "DISCRETE, ROTATE, 100, " + str(int(speed))
            w.send(movementCommand)
            #r.runCommand(movementCommand)
    #right
    elif (key == "d"):
        if (speed > 0 and speed <= 100):
            speedCommand = "CONTINUOUS, " + str(int(speed)) + ", " + str(int(-1*speed))
            w.send(speedCommand)
            #r.runCommand(speedCommand)
            movementCommand = "DISCRETE, ROTATE, 100, " + str(int(speed))
            w.send(movementCommand)
            #r.runCommand(movementCommand)
    #stop
    elif(key == "s"):
        speedCommand = "CONTINUOUS, 0, 0"
        w.send(speedCommand)
        movementCommand = "DISCRETE, ROTATE, 100, 0"
        w.send(movementCommand)
        return 0
    #set speed (1-0, 0 being 10)
    elif (key == "1"):
        return 10
    elif (key == "2"):
        return 20
    elif (key == "3"):
        return 30
    elif (key == "4"):
        return 40
    elif (key == "5"):
        return 50
    elif (key == "6"):
        return 60
    elif (key == "7"):
        return 70
    elif (key == "8"):
        return 80
    elif (key == "9"):
        return 90
    elif (key == "0"):
        return 100

def ReadingRainbow():
    key = ""
    speed = 0
    while (key != "m"):
        key = input("")
        speed = CommandConstruction(key, speed)
        

r = RobotControl()

ReadingRainbow()

