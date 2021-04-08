
import time
from mercury.driver.xbox_driver import XboxDriver

import time, threading
x = XboxDriver()
print(time.ctime())
threading.Timer(1, x.run).start()
x.signal()