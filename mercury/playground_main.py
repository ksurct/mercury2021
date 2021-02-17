

import requests
import time
for i in range(0,1):
    start = time.time()
    r = str(requests.get("https://script.google.com/macros/s/AKfycbzMSQjRxWl8jh1wGJHCdNgKcLCImKi5QqhUarJfdcwGahVCRU_NPeze/exec",{'name': "Quen"} ).content)
    print (r)
    print("Took: ", time.time() - start)