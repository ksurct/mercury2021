from mercury.settings.settings import settings
import sys
from time import sleep
settings.takeArgs(sys.argv)


print("Hello")

# comment

# comment
# dev branch

if (settings['instance'].value == 'realbot'):
    print('Running actual robot')
elif (settings['instance'].value == 'simbot'):
    print('Running simulation')
elif (settings['instance'].value == 'driver'):
    print('Running driving software')
else:
    print('Unknown setting')
while (True):
    print(".")
    sleep(0.5)