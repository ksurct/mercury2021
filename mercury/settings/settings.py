# This takes in a list of the arguments and parses for al listed settings, 

import sys

settings = {
    'instance': {
        'value': 'realRobot',
        'valid': {'realRobot','simRobot', 'driver'},
    },
}

def args(args):
    for i in range(0, len(args)):
        if (args[i].find("-") != -1 and args[i].replace('-', '') in settings): # makes sure the args are valid settings
            if (i < len(args) - 1): # if there is another argument for the setting
                if (True or args[i + 1] in settings[args[i].replace('-', '')]['valid']): # if 
                    settings[args[i].replace('-', '')]['value'] = args[i+1]
                else:
                    print("{} was an invalid argument for {}".format(args[i+1], args[i]))
                    print("Keeping original value....")
# run the argument program
args(sys.argv)
