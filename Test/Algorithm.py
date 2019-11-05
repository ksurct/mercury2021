# This is a comment
# This is a chicken wing
# This is the abstract class for all of the algorithm testing. This abstract class will take in an array of sensor values and output a array of 
# velocities

from abc import ABC, abstractmethod

class Algorithm(ABC):
    def __init__(self, sensors):
        self.sensors = sensors
        super().__init__()

    @abstractmethod
    def run_algorithm_step(self,sensors):
        pass

class example_algorithm(Algorithm):
    def run_algorithm_step(self, sensors):
        # Do stuff here lads
        wheels = [3 , 2]
        return wheels #some wheel velocities

class example_algorithm2(Algorithm):
    def run_algorithm_step(self, sensors):
        # Do stuff here lads
        wheels = [100 , 100]
        return wheels #some wheel velocities

ex_sensors = [3,2,1,3,4,1,2,3,4,5,3,2]

#wheels_trial_1 = example_algorithm(ex_sensors)
#wheels_trial_1.run_algorithm_step(ex_sensors)

listOfAlgos = [example_algorithm(ex_sensors), example_algorithm2(ex_sensors)]

for algo in listOfAlgos:
    print(algo.run_algorithm_step(ex_sensors))





