# This takes in a list of the arguments and parses for al listed settings, 

import sys


class AllSettings():
    def __init__(self, settings):
        self.settings = settings

    def getAll(self):
        return self.settings

    def __getitem__(self, name):
        print("it works")
        return self.get(name)

    def __setitem__(self, name, val):
        self.get(name).set(val)

    def get(self, name):
        for s in self.settings:
            if (s.name == name):
                return s
        print("No setting named '{}'".format(name))
        return None

    def takeArgs(self, args):
        for i in range(0, len(args)):
            if (args[i].find("-") != -1 and self[args[i].replace('-', '')] != None): # makes sure the args are valid settings
                if (i < len(args) - 1): # if there is another argument for the setting
                    self[args[i].replace('-', '')] = args[i+1]

class Setting():
    def __init__(self, name, defautVal, possibleVals):
        self.value = defautVal
        self.name = name
        self.possibleVals = possibleVals

    def set(self, newVal):
        if (newVal in self.possibleVals):
            self.value = newVal
        else:
            print("Invalid value '{}' for '{}'".format(newVal, self.name))
            print("Keeping original value: '{}'".format(self.value))


settings = AllSettings([
    Setting("instance", 'realbot', ['realbot', 'simbot', 'driver']),
])
