import RPi.GPIO as GPIO
from .pins import PINS, BUZZER_DURATION, BUZZER_FREQ
import time

def sound_buzzer():
    start_time = time.time()
    while time.time() - start_time < BUZZER_DURATION:
        GPIO.output(PINS['BUZZER'], GPIO.HIGH)
        time.sleep(1 / BUZZER_FREQ / 2)
        GPIO.output(PINS['BUZZER'], GPIO.LOW)
        time.sleep(1 / BUZZER_FREQ / 2)
    start_time = time.time()
    while time.time() - start_time < BUZZER_DURATION:
        GPIO.output(PINS['BUZZER'], GPIO.HIGH)
        time.sleep(1 / BUZZER_FREQ / 2.5)
        GPIO.output(PINS['BUZZER'], GPIO.LOW)
        time.sleep(1 / BUZZER_FREQ / 2.5)
    start_time = time.time()
    while time.time() - start_time < BUZZER_DURATION:
        GPIO.output(PINS['BUZZER'], GPIO.HIGH)
        time.sleep(1 / BUZZER_FREQ / 3)
        GPIO.output(PINS['BUZZER'], GPIO.LOW)
        time.sleep(1 / BUZZER_FREQ / 3)