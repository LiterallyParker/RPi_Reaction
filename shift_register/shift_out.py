import RPi.GPIO as GPIO
import time
from .pins import PINS
grace = 0.001

def shift_out(data):
    for i in range(8): # 1 byte
        bit = (data >> (7 - i)) & 0x01
        GPIO.output(PINS['DS'], bit)
        
        GPIO.output(PINS['SHCP'], GPIO.HIGH)
        time.sleep(grace)
        GPIO.output(PINS['SHCP'], GPIO.LOW)
        
    GPIO.output(PINS['STCP'], GPIO.HIGH)
    time.sleep(grace)
    GPIO.output(PINS['STCP'], GPIO.LOW)