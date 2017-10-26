import math

def diffractionParam (h, d, d1, d2, lambda_):
	# h : despeje
	# d : distancia total entre las torres
	# d1 : distancia a la obstrucción
	# d2 : distancia desde la obstrucción
	return h*math.sqrt(2*d/(lambda_*d1*d2))

def diffractionParamAprox (h, R1):
	# válida para v>-1
	# h : despeje
	# R1 : primer anillo de fresnel
	return math.sqrt(2)*h/R1

def diffraction(beamElevation, R1):
	# retorna el despeje con valores entre 0 y 1
	# (multiplicar por 100 para en porcentaje)
	# beamElevation : elevación del haz
	# R1 : primer radio de fresnel
	return beamElevation/R1