from pynput import keyboard
import os

motorSpeed = 50
lockySpeed = 5

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        if (key.char == 'w'):
            print("Character is w")
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        os.system('clear')
        return False

try:
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
except KeyboardInterrupt:
    print("Exiting program")

