import RPi.GPIO as GPIO
import time

from Led import Led
from Buzzer import Buzzer

# //Initialisation de notre GPIO 17 pour recevoir un signal
# //Contrairement à nos LEDs avec lesquelles on envoyait un signal
broche = 17
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(broche, GPIO.IN)

currentstate = 0
previousstate = 0

lightblue = Led(24)
lightred = Led(18)
buzzer = Buzzer(22)

# Boucle infini jusqu'à CTRL-C
while True:
    # Lecture du capteur
    currentstate = GPIO.input(broche)
    # Si le capteur est déclenché
    if currentstate == 1 and previousstate == 0:
        print("Mouvement detecte!")
        lightblue.on()
        lightred.off()
        buzzer.on()
        # En enregistrer l'état
        previousstate = 1
    # Si le capteur est s'est stabilisé
    elif currentstate == 0 and previousstate == 1:
        print("Pret")
        lightblue.off()
        lightred.on()
        buzzer.off()
        previousstate = 0
    # On attends 10ms
    time.sleep(0.01)

