import argparse
import math
import matplotlib.pyplot as plt
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

# altura de la torre emisora (m)
h_t1 = 15
# altura de la torre receptora(m)
h_t2 = 15

ht = h_t1 + A[0]
hr = h_t2 + A[-1]

#--------------------------------
# Señal

# Frecuencia [Hz]
f = 15*pow(10,6)
# Wave length [m]
lambda_ = c/f

# Ángulo de Reflexión
beta = math.pi

Rmod = 1

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

	# Creamos un arreglo para todos los valores del desfasaje al que le queremos
	# calcular las pérdidas
	deltaPhaseDeg = [0.001, 20, 45, 60, 90, 180, 270, 300, 340, 359.99]
	deltaPhaseRad = []
	for i in range(len(deltaPhaseDeg)):
		deltaPhaseRad.append(math.radians(deltaPhaseDeg[i]))

	# Calculamos las Pérdidas por reflexion para cada defasaje
	Lrfx = []
	for i in range(len(deltaPhaseRad)):
		Lrfx.append(-10*math.log10(1+math.pow(Rmod,2)+2*Rmod*math.cos(beta+deltaPhaseRad[i])))

	if(plot):
		plt.figure()
		plt.fill_between(deltaPhaseDeg,0, Lrfx)
		plt.title("Reflexion losses for different phase shifts (Question B)")
		plt.ylabel('Losses (dB)')
		plt.xlabel('Phase Shift (deg)')
		plt.grid(True)
		plt.draw()

	if (debug):
		printHeader('Reflection Losses for differente Phase Shifts')
		print("Phase Shift(deg)\tReflection Loss(dB)")
		for i in range(len(deltaPhaseDeg)):
			print(str(deltaPhaseDeg[i])+"°\t"+str(Lrfx[i])+" dB")
		print()
		print()
		# print('Phase difference: '+str(round(deltaPhase, 2))+' m')
		# print('Losses: '+str(round(Lrfx, 2))+' dB')


	#--------------------------------
	# C)
	#--------------------------------

	# Fije las antenas a 15 m de altura sobre el nivel de terreno, y desplace levemente
	# una de ellas para obtener los desfasajes anteriores. Calcule el desfasaje entre el
	# rayo directo y el reflejado si la otra antena también se ubica a 15 m sobre el nivel
	# de terreno. Varíe la altura de una de las antenas alrededor del valor indicado para
	# provocar las variaciones indicadas para el desfasaje.

	# altura de la torre emisora (m)
	h_t1 = 15
	# altura de la torre receptora(m)
	h_t2 = 15

	ht = h_t1 + A[0]

	hr = []
	hr.append(h_t2 + A[-1])

	# Calculamos el desfasaje para antenas con esa altura

	# Diferencia de fase (rad)
	deltaPhase_C = []
	deltaPhase_C.append((4*math.pi*ht*hr[-1])/(lambda_*dt))

	# Calculamos las pérdidas con ese desfasaje (dB)
	Lrfx_C = []
	Lrfx_C.append(-10*math.log10(1+math.pow(Rmod,2)+2*Rmod*math.cos(beta+deltaPhase_C[0])))

	# Aumentamos la altura de la antena receptora y observamos las pérdidas
	while(Lrfx_C[-1] < Lrfx[0]):
		hr.append(hr[-1] - 0.01)
		deltaPhase_C.append((4*math.pi*ht*hr[-1])/(lambda_*dt))
		aux = 1+math.pow(Rmod,2)+2*Rmod*math.cos(beta+deltaPhase_C[-1])
		Lrfx_C.append(-10*math.log10(1+math.pow(Rmod,2)+2*Rmod*math.cos(beta+deltaPhase_C[-1])))
		if(Lrfx_C[-1] < Lrfx_C[-2]):
			break

	# Invertimos el arreglo para colocar las alturas de menor a mayor
	hr = hr[::-1]
	deltaPhase_C = deltaPhase_C[::-1]
	Lrfx_C = Lrfx_C[::-1]

	# Disminuimos la altura de la antena receptora y observamos las pérdidas
	while(Lrfx_C[-1] < Lrfx[0]):
		hr.append(hr[-1] + 0.01)
		deltaPhase_C.append((4*math.pi*ht*hr[-1])/(lambda_*dt))
		aux = 1+math.pow(Rmod,2)+2*Rmod*math.cos(beta+deltaPhase_C[-1])
		Lrfx_C.append(-10*math.log10(1+math.pow(Rmod,2)+2*Rmod*math.cos(beta+deltaPhase_C[-1])))
		if(Lrfx_C[-1] < Lrfx_C[-2]):
			break

	if(plot):
		plt.figure()
		plt.fill_between(hr,0, Lrfx_C)
		plt.title("Reflexion losses changing receiver antenna's height (Question C)")
		plt.ylabel('Losses (dB)')
		plt.xlabel('Height (m)')
		plt.grid(True)
		plt.draw()

	if (debug):
		printHeader("Reflection Losses changing the receiver antenna's height")
		print("Receiver Antenna's Height(m)\tReflection Loss(dB)")
		for i in range(len(hr)):
			print(str(hr[i])+" m\t"+str(Lrfx_C[i])+" dB")
		print()
		print()

	#--------------------------------
	# D)
	#--------------------------------
	# De manera cualitativa, ¿qué intuye usted que sucedería si el índice troposférico
	# variase?

	# Observamos que con cambios de centímetros en la altura de la antena receptora
	# las pérdidas por reflexión cambian bruscamente. Por ejemplo, aumentando 5 cm
	# las pérdidas van de -5.98 dB a 25.12 dB. Y disminuyendo 4 cm las pérdidas van de
	# -5.98 dB a 12.01 dB. Intuimos que cualquier pequeño cambio en el índice troposférico
	# cambiaría con facilidad las pérdidas por reflexion en grán magnitud. Por lo tanto
	# es necesario proteger contra las pérdidas por reflexión en lugar de incluirlas
	# en los cálculos.

if __name__ == '__main__':
	main()
	# OJO!!! siempre dejar esto al final para que no se cierren los gráficos
	# no importa si no estás graficando
	profile.plotShow()
