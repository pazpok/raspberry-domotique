from ../flask import flask
app = Flask(__name__)

# import des utilistaires python
# import des utilistaires python
import RPi.GPIO as GPIO
import time


# Utilisation d'une norme de nommage pour les broches
def ledon():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(14, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)

    print("Led On")
    GPIO.output(14, GPIO.HIGH)
    GPIO.output(15, GPIO.HIGH)


def ledoff():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(14, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    print("Led Off")


GPIO.cleanup()

