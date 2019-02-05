from flask import Flask
from flask_socketio import SocketIO, send, emit
from flask import render_template
from light import Lumiere
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template('index.html')


#def message_loop():
#    while True:
#        message = input('Votre message ?')
#        socketio.emit('alert', message, Broadcast=True)

# Vue que notre méthode pour lire nos message est une boucle infinie
# Elle bloquerait notre serveur. Qui ne pourrait répondre à aucune requête.
# Ici nous créons un Thread qui va permettre à notre fonction de se lancer
# en parallèle du serveur.
light = Lumiere(27)

read_lum = threading.Thread(target=light.light_loop,args=(socketio,))
read_lum.start()
