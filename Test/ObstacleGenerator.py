import random


class ObstacleGenerator:

    def __init__(self):

        self.lengths = [12, 12, 24, 24, 36]
        self.maxx = 96
        self.maxy = 72
        self.points = []

    def generate(self):

        check = False

        while (check == False):

            for length in self.lengths:


#Random ChangeS
