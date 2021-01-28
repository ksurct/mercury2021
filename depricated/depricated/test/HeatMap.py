# HeatMay.py
# Author: Dustin Wilson

import plotly.graph_objects as go
import csv

# Creates a heat map of a given csv file
# Path is the location of the csv file
def HeatMap(path):

  # Number of rows in the csv file
  numRow = 0
  # Number of cols
  numCol = 0

  # Opens the csv file and reads in each line
  # Adds each line to the array
  # First pass is to know how big to intialize the array
  with open(path, newline='') as File:  
      reader = csv.reader(File)
      for row in reader:
          numCol = 0
          for indiv in row:
            numCol = numCol + 1
          numRow = numRow + 1
  
  # Intializes an array
  # Has zeros in all positions initially
  array = [[0 for i in range(numCol)] for j in range(numRow)]

  # Opens the csv file and reads in each line
  # Adds each line to the array
  # Second pass actually sets values
  with open(path, newline='') as File:  
      reader = csv.reader(File)
      i = 0
      for row in reader:
          j = 0
          for indiv in row:
            array[i][j] = indiv
            j = j + 1
          i = i + 1

  # Creates the heat map based on the array which is built from csv file
  fig = go.Figure(data=go.Heatmap(z = array))
  # Displays the figure
  fig.show()