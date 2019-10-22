# Generates a set of test courses which are valid
from ObstacleGenerator import *
from CsvHandler import *

numCourses = 1000

for i in range(numCourses):
    # The course generated with obstacles and has a solution
    course = ObstacleGenerator()
    course.generate()

    field = ObstacleField(72, 96, 24, 34, 24, 6, course.pointobjects)
    
    # Used to save the file
    csvObj = CsvHandler()
    csvObj.addFieldToTable(field)
    fileName = "Test" + str(i)
    print(fileName)
    csvObj.saveTableToFile(fileName)