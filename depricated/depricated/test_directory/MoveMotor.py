import RPi.GPIO as GPIO
from time import sleep

PWM_PINS = [18, 12, 13, 26]
DIR_PINS = [24, 7, 5, 6]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.setup(directionPin1, GPIO.OUT)
for pin in PWM_PINS:
    GPIO.setup(pin, GPIO.OUT)
    

pi_pwm = [GPIO.PWM(PWM_PINS[0], 1000),
          GPIO.PWM(PWM_PINS[1], 1000),
          GPIO.PWM(PWM_PINS[2], 1000),
          GPIO.PWM(PWM_PINS[3], 1000)
          ]
for pin in pi_pwm:
    pin.start(0)
while True:
    for index, pin in enumerate(PWM_PINS):
        pi_pwm[index].ChangeDutyCycle(0)
