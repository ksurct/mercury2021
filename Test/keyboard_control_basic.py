import keyboard

def leftForward(event):
	print("LEFT FORWARD")

def rightForward(event):
	print("RIGHT FORWARD")

def leftBack(event):
	print("LEFT BACK")

def rightBack(event):
	print("RIGHT BACK")

def leftStop(event):
	print("LEFT STOP")

def rightStop(event):
	print("RIGHT STOP")

keyboard.on_press_key('w', leftForward)
keyboard.on_press_key('s', leftBack)
keyboard.on_press_key('u', rightForward)
keyboard.on_press_key('j', rightBack)
keyboard.on_release_key('w', leftStop)
keyboard.on_release_key('s', leftStop)
keyboard.on_release_key('u', rightStop)
keyboard.on_release_key('j', rightStop)

try:
	while True:
		pass
except KeyboardInterrupt:
	keyboard.unhook_all()
	print("Everything unhooked")