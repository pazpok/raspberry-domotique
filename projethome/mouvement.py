import RPi.GPIO as GPIO
import time
from flask_socketio import SocketIO, send, emit
from Led import Led
from Buzzer import Buzzer

# //Initialisation de notre GPIO 17 pour recevoir un signal
# //Contrairement à nos LEDs avec lesquelles on envoyait un signal

lightblue = Led(24)
lightred = Led(18)
buzzer = Buzzer(22)


class Mouvement():
    def __init__(self, broche):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.broche = broche
        GPIO.setup(broche, GPIO.IN)

    def mouvement_loop(self, socketio):
        currentstate = 0
        previousstate = 0
        while True:
            currentstate = GPIO.input(self.broche)
            previousstate = 0
            lightblue.on()
            if currentstate == 1 and previousstate == 0:
                lightblue.off()
                lightred.light_blink()
                buzzer.buzzer_blink()
                socketio.emit('alert', 'Mouvement détecté', Broadcast=True)
                previousstate = 1
            elif currentstate == 0 and previousstate == 1:
                socketio.emit('alert', 'Prêt', Broadcast=True)
                previousstate = 0
            time.sleep(0.01)

