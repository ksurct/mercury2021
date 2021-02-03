from mercury.settings.settings import settings
import sys
from time import sleep
settings.takeArgs(sys.argv)


print("Hello")

# comment
<<<<<<< HEAD

# Quen made a change

=======
print("I've made a change!!!")
>>>>>>> 854741cc3431419ed2aa2bd2b4145e6ab18a2567
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