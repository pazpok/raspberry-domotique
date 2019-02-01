# import des utilistaires python
# import des utilistaires python
import RPi.GPIO as GPIO
import time


class Led():
    def __init__(self, broche):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.broche = broche

        GPIO.setup(broche, GPIO.OUT)

    def on(self):
        GPIO.output(self.broche, GPIO.HIGH)

    def off(self):
        GPIO.output(self.broche, GPIO.LOW)

    def blink(self):
        i = 0
        while i < 30:
            GPIO.output(self.broche, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(self.broche, GPIO.LOW)
            time.sleep(1)
            i = i + 1
