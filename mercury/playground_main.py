
import time
import requests
import time

from Webserver_Compter import webserver


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
w = webserver()
while (True):
    # send("computer {}".format(i))
    w.send("computer DISCRETE,   ROTATE, 90, 50{}".format(i))
    i = i + 1
    # time.sleep(3)

