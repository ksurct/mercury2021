
import time
import requests
import time

from Webserver_Compter import computer_webserver
from Webserver_Robot import robot_webserver
import time


#def send(string):
#    start = time.time()
#    r = str(requests.get("https://script.google.com/macros/s/AKfycbzMSQjRxWl8jh1wGJHCdNgKcLCImKi5QqhUarJfdcwGahVCRU_NPeze/exec",{'name': "Quen"} ).content)
#    # print (r)
#
#    data_from_blob = r.split(" ")
#
#    data_from_blob.pop(0)
#    data_string = " "
#    data_string = data_string.join(data_from_blob)
#
#    print(data_string)
#
#    print("Took: ", time.time() - start)

i = 0
c = computer_webserver()
r = robot_webserver()
while (True):
    # send("computer {}".format(i))
    c.send("DISCRETE,   ROTATE, 90, 50{}")
    # i = i + 1

    r.send("this is a message from the robot")
    # time.sleep(3)
    # this is just for testing remove for trying to run on Pi
    time.sleep(2)
