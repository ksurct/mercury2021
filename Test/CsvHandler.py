import csv
from ObstacleField import ObstacleField, Point

class CsvHandler:
    def __init__(self):
        self.rowNumber_ = 0
        self.table_ = []


    # This function adds the given ObstacleField to the internal table.
    def addFieldToTable(self, oField : ObstacleField):
        self.table_.append(oField.parseForCsv())


    # This function appends the data form the given csv file to the internal table. 
    def loadTableFromFile(self, fileName):
        with open(fileName, newline='') as csvfile:
            data = list(csv.reader(csvfile))
            for row in data:
                self.table_.append(list(map(int, row)))
            

    # This function can create a new file, or overwrite an existing file of the given name. 
    def saveTableToFile(self, fileName):
        with open(fileName, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(self.table_)


    # This function returns the 2D array representing the ObstacleField table.
    def returnListOfFields(self):
        return self.table_

    
    # This function clears the internal table.
    def clearInternalTable(self):
        self.table_ = []
        self.rowNumber_ = 0


    # This function prints the ObstacleField Table.
    def toString(self):
        print(self.table_)
                
        

if __name__ == "__main__":
    # You can choose to only specify the points this way, and keep the default arguments
    testField = ObstacleField(occupiedPoints=[Point(3,3), Point(3,4)])
    
    csvObj = CsvHandler()
    csvObj.addFieldToTable(testField)
    csvObj.addFieldToTable(testField)
    csvObj.saveTableToFile("Test0.csv")
    csvObj.toString()
    csvObj.clearInternalTable()
    csvObj.toString()
    csvObj.loadTableFromFile("Test0.csv")
    csvObj.loadTableFromFile("Test0.csv")
    csvObj.toString()
