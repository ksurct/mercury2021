from mercury.settings.settings import settings
import sys
print("This module is working.")

settings.takeArgs(sys.argv)

for setting in settings.getAll():
    print(setting.value)