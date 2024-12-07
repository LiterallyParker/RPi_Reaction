import RPi.GPIO as GPIO
from .pins import PINS

def blue_off():
    GPIO.output(PINS['BLUE_LED'], GPIO.LOW)
    return False