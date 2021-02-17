
import time
import requests
import time

from mercury.Webserver_Compter import webserver
def send(string):
    start = time.time()
    r = str(requests.get("https://script.google.com/macros/s/AKfycbyeRPqV1Z0vLX7ztAjCxlQ10JlUnFOmEw3ml2W7MuUaXyrOibkZSSDbjw/exec",{'blob': string} ).content)
    print (r)
    print("Took: ", time.time() - start)
i = 0
w = webserver()
while (True):
    # send("computer {}".format(i))
    w.send("computer {}".format(i))
    i = i + 1
    # time.sleep(3)
    

