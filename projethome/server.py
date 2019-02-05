from flask import Flask
from flask import render_template
from flask_socketio import SocketIO, send, emit
from mouvement import Mouvement
from TemperatureSensor import TemperatureSensor
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template('index.html')


#def message_loop():
#    while True:
#        message = input('Mouvement détecté')
#        socketio.emit('alert', message, Broadcast=True)

# Vue que notre méthode pour lire nos message est une boucle infinie
# Elle bloquerait notre serveur. Qui ne pourrait répondre à aucune requête.
# Ici nous créons un Thread qui va permettre à notre fonction de se lancer 
# en parallèle du serveur.
#read_messages = threading.Thread(target=message_loop)
#read_messages.start()

mouvement = Mouvement(17)
temp_c = TemperatureSensor()

read_mouvement = threading.Thread(target=mouvement.mouvement_loop,args=(socketio,))
read_mouvement.start()

#read_temperature = threading.Thread(target=temp_c.temperature_loop,args=(socketio,))
#read_temperature.start()
