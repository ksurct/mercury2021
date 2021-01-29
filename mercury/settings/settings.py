# This takes in a list of the arguments and parses for al listed settings, 

import sys

class AllSettings():
    def __init__(self, settings):
        self.settings = settings

    def getAll(self):
        return self.settings

    def get(self, name):
        for s in self.settings:
            if (s.name == name):
                return s
        return None

    def takeArgs(self, args):
        for i in range(0, len(args)):
            if (args[i].find("-") != -1 and settings.get(args[i].replace('-', '')) != None): # makes sure the args are valid settings
                if (i < len(args) - 1): # if there is another argument for the setting
                    settings.get(args[i].replace('-', '')).setVal(args[i+1])

class Setting():
    def __init__(self, name, defautVal, possibleVals):
        self.value = defautVal
        self.name = name
        self.possibleVals = possibleVals

    def setVal(self, newVal):
        if (newVal in self.possibleVals):
            self.value = newVal
        else:
            print("Invalid value '{}' for '{}'".format(newVal, self.name))
            print("Keeping original value: '{}'".format(self.value))


settings = AllSettings([
    Setting("instance", 'realbot', ['realbot', 'simbot', 'driver']),
])
