import requests

class InternetCom:
    def __init__(self, id = "robot", url = "http://127.0.0.1:8000/server"):
        self.prevId = 0
        self.url = url
        self.i = 0
        self.id = id

    def send(self, string):
        r = str(requests.get("{}/{},{},{}/".format(self.url, self.id, self.i, string)).content.decode("utf-8"))
        data_from_blob = r.split(",")
        print(r)
        self.i = self.i + 1
        if data_from_blob[0] == self.prevId:
            return ""
        else:
            self.prevId = data_from_blob[0]
        return r

if (__name__ == "__main__"):
    import time
    it = InternetCom()
    while (True):
        print("From it: ", it.send("test"))
        time.sleep(1)