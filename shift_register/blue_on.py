import RPi.GPIO as GPIO
from .pins import PINS
    
def blue_on():
    GPIO.output(PINS['BLUE_LED'], GPIO.HIGH)
    return True