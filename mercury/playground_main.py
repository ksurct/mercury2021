

import requests
import time
for i in range(0,1):
    start = time.time()
    r = str(requests.get("https://script.google.com/macros/s/AKfycbzMSQjRxWl8jh1wGJHCdNgKcLCImKi5QqhUarJfdcwGahVCRU_NPeze/exec",{'name': "Quen"} ).content)
    # print (r)

    data_from_blob = r.split(" ")

    data_from_blob.pop(0)
    data_string = " "
    data_string = data_string.join(data_from_blob)

    print(data_string)

    print("Took: ", time.time() - start)