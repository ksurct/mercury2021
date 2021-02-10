from time import time

# This must be imported at the start of time.
class TimeKeeper():
    startTime = time()
    
    @staticmethod
    def currentTime():
        return time()

    # Gets milliseconds since start of program
    @staticmethod
    def millis():
        return (time() - TimeKeeper.startTime) * 1000