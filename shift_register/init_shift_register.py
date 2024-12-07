import RPi.GPIO as GPIO
from .pins import PINS

def init_shift_register():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PINS['DS'], GPIO.OUT)
    GPIO.setup(PINS['SHCP'], GPIO.OUT)
    GPIO.setup(PINS['STCP'], GPIO.OUT)
    GPIO.setup(PINS['BLUE_LED'], GPIO.OUT)
    GPIO.setup(PINS['BUZZER'], GPIO.OUT)
    
    GPIO.output(PINS['DS'], GPIO.LOW)
    GPIO.output(PINS['SHCP'], GPIO.LOW)
    GPIO.output(PINS['STCP'], GPIO.LOW)
    GPIO.output(PINS['BLUE_LED'], GPIO.LOW)
    GPIO.output(PINS['BUZZER'], GPIO.LOW)