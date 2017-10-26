from math import pow, pi


def powerReceive (lambda_, Ptx, gtx, grx, d):
	# lambda_ : longitud de onda en km
	# Ptx : potencia transmitida
	# g1, g2 : ganancias de las anteas
	# d1 : distancia entre las antenas

	return Ptx*gtx*grx*pow(lambda_, 2)/pow(4*pi*d, 2)


def sumPowerLosses (Ptx, G, L):
	# Ptx : potencia de transmisión dB
	# G : arreglo con las ganancias de las antenas dB
	# L : arreglo con las perdidas de todo el sistema dB

	return Ptx+sum(G)-sum(L)

def MargenFading (Pr, Srx):
	return (Pr-Srx) >= 20

def checkDisponibilidad (Pr, Srx):
	return MargenFading(Pr, Srx)