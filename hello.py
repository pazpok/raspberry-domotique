from Led import Led

from flask import render_template

from flask import Flask
app = Flask(__name__)

lightr = Led(14)
lightb = Led(15)

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
