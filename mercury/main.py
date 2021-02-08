from mercury.settings.settings import settings
import sys
from time import sleep
settings.takeArgs(sys.argv)

if (settings['instance'].value == 'realbot'):
    import mercury.real_main
elif (settings['instance'].value == 'simbot'):
    import mercury.sim_main
elif (settings['instance'].value == 'driver'):
    import mercury.driver_main
else:
    print('Unknown setting')