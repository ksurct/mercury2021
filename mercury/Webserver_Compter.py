import requests
import time


class computer_webserver:
    def __init__(self):
        self.Same_data = 0
        self.i = 0
        pass

    def send(self, string):

        print("------------------COMPUTER-------------------")

        print("Data being sent by computer: computer " + str(self.i) + " " + string)

        start = time.time()
        r = str(requests.get("http://10.150.251.154:8000/server/computer,{}".format(string)).content)
        print("Took: ", time.time() - start)

        data_from_blob = r.split(" ")
        print("Data read from Robot: ", data_from_blob)

        self.i = self.i + 1

        if self.i > 10:
            self.i = 0

        if data_from_blob[1] == self.Same_data:
            print("Instructions did not change")
            pass

        return data_from_blob
