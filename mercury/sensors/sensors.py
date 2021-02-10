from mercury.time.time_keeper import TimeKeeper
class Sensor():
    def __init__(self, name):
        self.name = name
        self._timeOfLastUpdate = -1
        self._distance = -1

    def update(self, distance):
        self._distance = distance
        self._timeOfLastUpdate = TimeKeeper.millis()

    def getDistance(self):
        return self._distance

    def getTimeOfLastUpdate(self):
        return self._timeOfLastUpdate