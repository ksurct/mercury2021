import requests
import time


class robot_webserver:
    def __init__(self):
        self.Same_data = 0
        self.i = 0
        pass

    def send(self, blob_to_send):
        print("---------------ROBOT--------------")

        print("Data being sent by robot: robot " + str(self.i) + " " + blob_to_send)

        start = time.time()
        r = str(requests.get("https://script.google.com/macros/s/AKfycbyeRPqV1Z0vLX7ztAjCxlQ10JlUnFOmEw3ml2W7MuUaXyrOibkZSSDbjw/exec", {'blob': "robot " + str(blob_to_send)}).content)
        print("Took: ", time.time() - start)

        data_from_blob = r.split(" ")

        self.i = self.i + 1

        if self.i > 10:
            self.i = 0

        if data_from_blob[1] == self.Same_data:
            print("Instructions did not change")
            return ""


        self.Same_data = data_from_blob[1]
        print(r)
        return r
