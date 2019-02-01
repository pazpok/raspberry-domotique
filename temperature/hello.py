from flask import Flask
app = Flask(__name__)

from TemperatureSensor import TemperatureSensor

from Led import Led

from flask import render_template

lightr = Led(18)
lightb = Led(24)

pierre = TemperatureSensor()

@app.route('/hello')
def hello_world():
	return 'Hello World!'
@app.route('/')
def index():
	return render_template('base.html')
@app.route('/<bleu_rouge>/<on_off>')
def ledonb(bleu_rouge, on_off):
	if on_off == 'on' and bleu_rouge == 'bleu':
		lightb.on()
	elif on_off == 'off' and bleu_rouge == 'bleu':
		lightb.off()
	elif on_off == 'on' and bleu_rouge == 'rouge':
		lightr.on()
	elif on_off == 'off' and bleu_rouge == 'rouge':
		lightr.off()
	else:
		return 'BLC'
	return render_template('base.html')
@app.route('/blink')
def ledblink():
	lightr.blink()
	lightb.blink()
	return render_template('base.html')
@app.route('/temperature')
def temperature():
	temp_c = pierre.read_celcius()
	temp_f = pierre.read_fahrenheit()
	if temp_c < 20:
            lightb.on()
            lightr.off()
            return render_template('base.html', temp_c=temp_c, temp_f=temp_f)
	elif temp_c > 30:
            lightb.off()
            lightr.on()
            return render_template('base.html', temp_c=temp_c, temp_f=temp_f)
	else:
            lightb.on()
            lightr.on()
            return render_template('base.html', temp_c=temp_c, temp_f=temp_f)
	return render_template('base.html', temp_c=temp_c, temp_f=temp_f)
