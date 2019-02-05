import RPi.GPIO as GPIO
import time
from flask_socketio import SocketIO, send, emit


class Lumiere():
    def __init__(self, broche):
        self.broche = broche
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def read_light(self):
        lightCount = 0  # intitialisation de la variable de lumière
        GPIO.setup(self.broche, GPIO.OUT)
        GPIO.output(self.broche, GPIO.LOW)
        time.sleep(0.1)  # on draine la charge du condensateur
        GPIO.setup(self.broche, GPIO.IN)
        # Tant que la broche lit ‘off’ on incrémente notre variable
        while (GPIO.input(self.broche) == GPIO.LOW):
            lightCount += 1
        return lightCount

    def light_loop(self, socketio):
        while True:
            socketio.emit('alert', self.read_light(), Broadcast=True)
            time.sleep(0.5)

