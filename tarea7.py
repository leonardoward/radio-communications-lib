import argparse
import math
from printColors import printHeader, printSubHeader, printWarning, printOK, printFail
from RadiocomLib import profile

#----------------------------------------------------------------
# Default values and pre-load example
#----------------------------------------------------------------

#--------------------------------
# Constantes

# velocidad de la luz [m/s]
c = 3*pow(10, 8)

#--------------------------------
# Datos del perfil

# d en Km
d = [0, 0.5, 1.5, 1.8, 2.5, 3, 4, 8, 8.5]
# A en m
A = [900, 850, 700, 750, 675, 650, 600, 600, 650]
# distancia total
dt = d[-1]

# índice troposférico
k = 0.45

#--------------------------------
# Antenas

# altura de la torre emisora
h_t1 = 1
# altura de la torre receptora
h_t2 = 1

ht = h_t1 + A[0]
hr = h_t2 + A[-1]

#--------------------------------
# Señal

# Frecuencia [Hz]
f = 15*pow(10,6)
# Wave length [m]
lambda_ = c/f

# Ángulo de Reflexión
beta = 1

R = -1

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser(
	description='Script to calculate reflexion in a communications system',
	epilog='''Example usage: 
		python3 tarea7.py -k 0.4 -f 15''')
ap.add_argument("-k", "--atmospheric-index", help="Set atmospheric index to profile corrections", default=k)
ap.add_argument("-f", "--frequency", help="Set signal frequency in MHz", default=f)
ap.add_argument("-p", "--plot", help="Show plots (True or False / t or f)", default=k)
ap.add_argument("-d", "--debug", help="Debug (True or False)", default=False)
args = vars(ap.parse_args())

# get arguments
k = float(args['atmospheric_index'])

if (args["debug"] in ('True', 'true', 't', 'T', 'y', 'Y')):
    debug = True
else:
    debug = False

if (args["plot"] in ('True', 'true', 't', 'T', 'y', 'Y')):
	plot = True
else:
    plot = False

def main():

	#--------------------------------
	# A)
	#--------------------------------

	p = profile.calcProfileFullCorrection(d, A, k, debug=debug)

	if (plot):
		profile.plotProfileArrays(1, d, 'm', A, 'Km', title="without corrections")
		profile.plotProfileArrays(2, d, 'm', p, 'Km', title="with corrections")

	#--------------------------------
	# B)
	#--------------------------------

	# Diferencia de fase (rad)
	deltaPhase = (4*math.pi*ht*hr)/(lambda_*dt)

	# Pérdidas por reflexion
	Lrfx = -10*math.log10(1+math.pow(math.fabs(R),2)+2*math.fabs(R)*math.cos(beta+deltaPhase))

	if (debug):
		printHeader('Reflection Losses')
		print('Phase difference: '+str(round(deltaPhase, 2))+' m')
		print('Losses: '+str(round(Lrfx, 2))+' dB')


	#--------------------------------
	# C)
	#--------------------------------

	#--------------------------------
	# D)
	#--------------------------------

	# Diferencia de Recorrido
	TPR = math.sqrt(math.pow(dt,2)+math.pow(ht+hr,2))
	TR = math.sqrt(math.pow(dt,2)+math.pow(ht-hr,2))
	deltaL = TPR - TR




if __name__ == '__main__':
	main()
	# OJO!!! siempre dejar esto al final para que no se cierren los gráficos
	# no importa si no estás graficando
	profile.plotShow()
