import math
from printColors import printWarning, printFail, printHeader


def waveGuide (alpha, largo):
	# alpha: pérdidas/100 metros (dB/m)
	# largo: longitud de la guía de onda (m)

	return largo*alpha/100

def lluvia (alpha, largo):
	# alpha: pérdidas/100 metros (dB/Km)
	# largo: longitud de la guía de onda (Km)

	return largo*alpha

def passiveRepeter (f, d1, d2):
	# f : frecuencia de la señal en GHz
	# d1, d2 : distancias hasta y desde la repetidora en Km
	printWarning("PassiveRepeater: remember that frequency must be in GHz")
	printWarning("PassiveRepeater: remember that distances must be in Km")
	print("\n")

	d = math.sqrt(d1*d2)
	return 2*(92.45 + 20*math.log10(f)+20*math.log10(d))


# AUN NO ESTA LISTA
def fullPassisveRepeter (f, pt, G, distances):
	# f : frecuencia de la señal en GHz
	# d1, d2 : distancias hasta y desde la repetidora en Km
	# pt1 : potencia de transmisión en dB
	# G : arreglo de ganancias de cada una de las antenas en dB
	return pt + sum(G) - passiveRepeater(f, d1, d2)

def diffraction (v):
	# diffraction losses
	# v : parámetro de difracción:
	return 6.9 + 20*math.log10(math.sqrt(math.pow(v-0.1, 2)+1)+v-0.1)
