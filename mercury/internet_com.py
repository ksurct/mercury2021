import requests

class InternetCom:
    def __init__(self, id = "robot", url = "http://127.0.0.1:8000/server"):
        self.Same_data = 0
        self.url = url
        self.i = 0
        self.id = id

    def send(self, string):
        r = str(requests.get("{}/{},{},{}/".format(self.url, self.id, self.i, string)).content.decode("utf-8"))
        data_from_blob = r.split(",")
        print(r)
        self.i = self.i + 1
        if data_from_blob[0] == self.Same_data:
            return ""
        else:
            self.Same_data = data_from_blob[0]
            print("SETTING to ", self.Same_data)
        
        return r

import time
if (__name__ == "__main__"):
    it = InternetCom()
    while (True):
        print("From it: ", it.send("test"))
        time.sleep(1)