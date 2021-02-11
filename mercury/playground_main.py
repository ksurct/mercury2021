# Write anything in this to test your code.
from mercury.time.time_keeper import TimeKeeper
from time import sleep
from mercury.robot_control.real_robot_control import RealRobotControl

r = RealRobotControl()

r.setAllMotorSpeeds(100)

r.move(1, 0.25)

import requests
import time
for i in range(0,1):
    start = time.time()
    r = str(requests.get("https://script.googleusercontent.com/macros/echo?name=caden&country=&user_content_key=rFOnik81IF7SCA_glS3nRDDvpe9TfyyuDCXc8Mk_WQ-Cpr9xGgxtruzXz2gIkmlB2tP2fIObTlB5ymsgMsqyQNQzmOGi_uSim5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnA8lsD2hzW1wPY5pPWAaKJ0DZVaUButaeRmNqM0t6EmHpVlC-BhyAfrPezVolMEld49r0iaiSPzpvJsw0wqpxiI&lib=Max2NL1KXXIisUHgDNWFENrEZxPVCO64K",{'name': "Caden"} ).content)
    print (r)
    print("Took: ", time.time() - start)