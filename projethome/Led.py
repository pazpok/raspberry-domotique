import threading
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
        time.sleep(1)
        GPIO.output(self.broche, GPIO.LOW)

    def off(self):
        GPIO.output(self.broche, GPIO.LOW)

    def blink(self):
        i = 0
        while i < 10:
            GPIO.output(self.broche, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(self.broche, GPIO.LOW)
            time.sleep(0.1)
            i = i + 1

    def light_blink(self):
        blinklr = threading.Thread(target=self.blink)
        blinklr.start()

