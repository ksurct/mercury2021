import requests
import time

class webserver:

    def __init__(self):
        pass

    def send(self, string):

        start = time.time()
        r = str(requests.get("http://24.248.230.205:8000/server/computer,this,is,a,test/").content)
        print("Took: ", time.time() - start)

        # print(r)

        data_from_blob = r.split(" ")
        print("data being read in", data_from_blob)
        return data_from_blob
        # for x in range(len(data_from_blob)):
        #     data_cell_strip1 = data_from_blob[x].strip("'")
        #     data_cell_strip2 = data_cell_strip1.strip(' "b')
        #     robot_data = data_cell_strip2.strip("'")

        #     # print(robot_data)
        #     list1.append(robot_data)

        #     return list1



# if __name__ == "__main__":
#     d1 = webserver("computer arm", "")
#     data = d1.send()
#     for d in range(len(data)):
#         print(data)


