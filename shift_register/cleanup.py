import RPi.GPIO as GPIO

def cleanup():
    print("Cleaning...")
    GPIO.cleanup()
    