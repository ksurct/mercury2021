import requests
import time

class webserver:

    def __init__(self):
        pass

    def send(self, string):

        i = 0

        start = time.time()
        r = str(requests.get("https://script.google.com/macros/s/AKfycbyeRPqV1Z0vLX7ztAjCxlQ10JlUnFOmEw3ml2W7MuUaXyrOibkZSSDbjw/exec",{'blob': i + string} ).content)
        print("Took: ", time.time() - start)

        # print(r)

        data_from_blob = r.split(" ")
        print("data being read in", data_from_blob)

        i = i + 1

        if i > 10:
            i = 0

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


