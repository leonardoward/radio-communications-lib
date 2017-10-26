import math

def waveGuide (alpha, largo):
	# alpha: pérdidas/100 metros (dB/m)
	# largo: longitud de la guía de onda (m)

	return largo*alpha/100

def passiveRepeater (f, d1, d2):
	# f : frecuencia de la señal en GHz
	# d1, d2 : distancias hasta y desde la repetidora en Km
	print("PassiveRepeater: remember that frequency must be in GHz")
	print("PassiveRepeater: remember that distances must be in Km")

	d = math.sqrt(d1, d2)
	return = 2*(92.45 + 20*math.log10(f)+20*math.log10(d))

def fullPassisveRepeter (f, pt1, G, d1, d2):
	# f : frecuencia de la señal en GHz
	# d1, d2 : distancias hasta y desde la repetidora en Km
	# pt1 : potencia de transmisión en dB
	# G : arreglo de ganancias de cada una de las antenas en dB
	return pt1 + sum(G) - passiveRepeater(f, d1, d2)

def diffraction (v):
	# diffraction losses
	# v : parámetro de difracción:
	return 6.9 + 20*math.log10(math.sqrt(math.pow(v-0.1, 2)+1)+v-0.1)
