
import time
import requests
import time

from mercury.Webserver_Compter import webserver
def send(string):
    start = time.time()
<<<<<<< HEAD
    r = str(requests.get("https://script.google.com/macros/s/AKfycbzMSQjRxWl8jh1wGJHCdNgKcLCImKi5QqhUarJfdcwGahVCRU_NPeze/exec",{'name': "Quen"} ).content)
    # print (r)

    data_from_blob = r.split(" ")

    data_from_blob.pop(0)
    data_string = " "
    data_string = data_string.join(data_from_blob)

    print(data_string)

    print("Took: ", time.time() - start)
=======
    r = str(requests.get("https://script.google.com/macros/s/AKfycbyeRPqV1Z0vLX7ztAjCxlQ10JlUnFOmEw3ml2W7MuUaXyrOibkZSSDbjw/exec",{'blob': string} ).content)
    print (r)
    print("Took: ", time.time() - start)
i = 0
w = webserver()
while (True):
    # send("computer {}".format(i))
    w.send("computer DISCRETE,   ROTATE, 90, 50{}".format(i))
    i = i + 1
    # time.sleep(3)
    

>>>>>>> 3de17b4374cf2e6930ab31194496dc0e583470c7
