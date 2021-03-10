import requests
import time





class robot_webserver:
    def __init__(self):
        self.Same_data = 0
        self.i = 0
        pass

    def send(self, blob_to_send):
        print("---------------ROBOT--------------")
        list1 = []
        start = time.time()
        r = str(requests.get("https://script.google.com/macros/s/AKfycbyeRPqV1Z0vLX7ztAjCxlQ10JlUnFOmEw3ml2W7MuUaXyrOibkZSSDbjw/exec", {'blob': "robot " + str(blob_to_send)}).content)
        print("Took: ", time.time() - start)



        data_from_blob = r.split(" ")



        if data_from_blob[1] == self.Same_data:
            print("Instructions did not change")
            return

        self.Same_data = data_from_blob[1]

        print("Data read from Computer: ", r)
        #print(data_from_blob)

        # for x in range(len(data_from_blob)):
        #    data_cell_strip1 = data_from_blob[x].strip("'")
        #    data_cell_strip2 = data_cell_strip1.strip(' "b')
        #    robot_data = data_cell_strip2.strip("'")
        # print(robot_data)
        #   list1.append(robot_data)


