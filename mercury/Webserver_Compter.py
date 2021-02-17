import requests
import time

class webserver:
    list1 = []
    def __init__(self, blob_to_send, list1):



        self.blob_to_send = blob_to_send
        self.list1 = list1

    def send(self):

        list1 =[]
        start = time.time()
        r = str(requests.get("https://script.google.com/macros/s/AKfycbyeRPqV1Z0vLX7ztAjCxlQ10JlUnFOmEw3ml2W7MuUaXyrOibkZSSDbjw/exec",{'blob': self.blob_to_send} ).content)
        print("Took: ", time.time() - start)

        print(r)

        data_from_blob = r.split(" ")
        print(data_from_blob)

        for x in range(len(data_from_blob)):
            data_cell_strip1 = data_from_blob[x].strip("'")
            data_cell_strip2 = data_cell_strip1.strip(' "b')
            robot_data = data_cell_strip2.strip("'")

            print(robot_data)
            list1[x-1].append(robot_data)

            return self.list1



if __name__ == "__main__":
    d1 = webserver("computer arm", "")
    data = d1.send()
    print(data)