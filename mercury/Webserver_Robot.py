import requests
import time

Same_data = 0

def send(blob_to_send):
    list1 = []
    start = time.time()
    r = str(requests.get("https://script.google.com/macros/s/AKfycbyeRPqV1Z0vLX7ztAjCxlQ10JlUnFOmEw3ml2W7MuUaXyrOibkZSSDbjw/exec", {'blob': blob_to_send}).content)
    print("Took: ", time.time() - start)

    print(r)

    data_from_blob = r.split(" ")

    if data_from_blob[1] == Same_data:
        return

    print(data_from_blob)

    # for x in range(len(data_from_blob)):
    #    data_cell_strip1 = data_from_blob[x].strip("'")
    #    data_cell_strip2 = data_cell_strip1.strip(' "b')
    #    robot_data = data_cell_strip2.strip("'")
    # print(robot_data)
    #   list1.append(robot_data)


send("robot this is a message from the robot")
