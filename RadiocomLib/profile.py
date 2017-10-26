import matplotlib.pyplot as plt
import pandas as pd
import sys

def plotProfileCSV(csv, k):

	if (k < 0):
		print("K debe ser mayor que 0")
		sys.exit()

	# load data
	data = pd.read_csv(csv)

	distance = data.Distance
	elevation = data.Elevation
	
	distance = distance.tolist()
	elevation = elevation.tolist()

	# k = float(input('Índice atmosférico: '))

	distance_ = []
	# convert from m to m
	for i in range(0, len(distance)):
		distance_.append(distance[i]/1000)

	# curvaturas por difracción
	protuberancia = B_k(distance_, k)

	# curvaturas por perturbación terrestre
	protuberancia1 = B_e(distance_)

	final_elevation = []
	
	[final_elevation.append(x + y + z) for x, y, z in zip(elevation, protuberancia, protuberancia1)]

	# without index atmospheric
	# plot(1, 'Topographic Profile', distance, elevation)

	# only with index atmospheric
	# plot(2, 'Topographic Profile (Perturbaciones terrestres)', distance, protuberancia)

	# 04141519508

	# only with index atmospheric
	# plot(3, 'Topographic Profile (Perturbaciones por refracción)', distance, protuberancia1)

	# final
	plot(4, 'Topographic Profile (Final)', distance, final_elevation)

	plt.show()

	# # Datos para calcular el radio de Fresnel
	# f = 12770000
	# lambda_ = 300000000/f

	# # San Bernardino
	# pxA = 0
	# pyA = 909

	# #Primera Repetidora:
	# pxR1 =  7456
	# pyR1 = 1259

	# # Segunda Repetidora:
	# pxR2 = 21080
	# pyR2 = 485

	# # Tacoa
	# pxB = 23092
	# pyB = 185

	#               # 1er tramo        # 2do tramo
	# # pxObstacles = [4022, 4790, 10846, 15139, 17127]
	# # pyObstacles = [1037, 1059, 907, 732, 593]

	#                # 1er tramo        # 2do tramo
	# pxObstacles = [15244, 17189, 17958]
	# pyObstacles = [732, 657, 564]

	# pxAntena1 = pxR1
	# pyAntena1 = pyR1
	# hAntena1 = 80
	# pyAntena1 = hAntena1 + pxAntena1

	# pxAntena2   = pxR2
	# pyAntena2   = pyR2
	# hAntena2 = 80
	# pyAntena2 = pyAntena2 + hAntena2

	# # Ecuación de la recta
	# m = (pyAntena2 - pyAntena1)/(pxAntena2 - pxAntena1)
	# # b = pyAntena1 

	# # print("m = "+str(m))
	# # print("b = "+str(b))
	# hazPoints = []

	# for x in range(pxAntena1,pxAntena2):
	#     newY = m*(x - pxAntena1) + pyAntena1
	#     # print(x)
	#     # newY = m*x + b
	#     for i in range(len(pxObstacles)):
	#         # print(pxObstacles[i])
	#         # print(x)
	#         if(pxObstacles[i] == x):
	#             # print(x)
	#             # print((lambda_*(x - pxAntena1)*(pxAntena2 - x))/(pxAntena2-pxAntena1))
	#             d1 = x - pxAntena1
	#             d2 = pxAntena2 - x
	#             d = pxAntena2 - pxAntena1

	#             rFresnel = math.sqrt((lambda_*(x - pxAntena1)*(pxAntena2 - x))/(pxAntena2-pxAntena1))
	#             print("x = " + str(x))
	#             print("d = "+ str(d))
	#             print("d1 = "+ str(d1))
	#             print("d2 = "+ str(d2))
	#             print("Altura del obstaculo = " + str(pyObstacles[i]))
	#             print("Radio de Fresnel = " + str(rFresnel))
	#             print("Altura del Haz = " + str(newY))
	#             deltaH = newY - (pyObstacles[i] + rFresnel)
	#             print("Altura del Haz - (Altura del obstaculo + radio de Fresnel) = " + str(deltaH))
	#             if(deltaH < 0):
	#                 print("Error")


	#     hazPoints.append(newY)

# regresa la nueva elevación tomando en cuenta sólo la corrección de la curvatura de la tierra
def calcProfileEarthCorrection(distance, elevation):
	if (len(distance) > len(elevation)):
		print("distancie[] tiene más elementos que elevation[]")
		sys.exit()
	elif (len(distance) < len(elevation)):
		print("elevation[] tiene más elementos que distance[]")
		sys.exit()

	# curvaturas por perturbación terrestre
	protuberancia1 = B_e(distance)

	final_elevation = []
	
	[final_elevation.append(x + y) for x, y in zip(elevation, protuberancia1)]

	print("Distance, Elevation")
	[print(str(d) + " , " + str(A)) for d, A in zip(distance, final_elevation)]
	print("\n")
	# return (final_elevation, protuberancia1)   # por si las moscas se necesita el valor de la protuberancia
	return final_elevation

# regresa la nueva elevación tomando en cuenta sólo la corrección de la refracción ambiental
def calProfileRefractionCorrection(distance, elevation, k):
	if (len(distance) > len(elevation)):
		print("distancie[] tiene más elementos que elevation[]")
		sys.exit()
	elif (len(distance) < len(elevation)):
		print("elevation[] tiene más elementos que distance[]")
		sys.exit()

	# curvaturas por difracción
	protuberancia = B_k(distance, k)

	final_elevation = []
	
	[final_elevation.append(x + y) for x, y in zip(elevation, protuberancia)]

	print("Distance, Elevation")
	[print(str(d) + " , " + str(A)) for d, A in zip(distance, final_elevation)]
	print("\n")
	# return (final_elevation, protuberancia)   # por si las moscas se necesita el valor de la protuberancia
	return final_elevation

def calcProfileFullCorrection(distance, elevation, k):
	if (len(distance) > len(elevation)):
		print("distancie[] tiene más elementos que elevation[]")
		sys.exit()
	elif (len(distance) < len(elevation)):
		print("elevation[] tiene más elementos que distance[]")
		sys.exit()

	# curvaturas por difracción
	protuberancia = B_k(distance, k)

	# curvaturas por perturbación terrestre
	protuberancia1 = B_e(distance)

	final_elevation = []
	
	[final_elevation.append(x + y) for x, y in zip(elevation, protuberancia)]

	print("Distance, Elevation")
	[print(str(d) + " , " + str(A)) for d, A in zip(distance, final_elevation)]
	print("\n")

	# corrección, protuberancia por difracción, protuberancia por curvatura de la tierra
	# return (final_elevation, protuberancia, protuberancia1)   # por si las moscas se necesita el valor de la protuberancia
	return final_elevation

def plotProfileArrays(n, distance, elevation, title=""):

	if(title == ""):
		title = "Topographic Profile"
	else:
		title = "Topographic Profile ("+str(title)+")"

	plt.figure(n)
	plt.fill_between(distance,0, elevation)
	plt.title(title)
	plt.ylabel('Elevation (m)')
	plt.xlabel('Distance (m)')
	plt.grid(True)
	plt.draw()

def plotShow():
	plt.show()

def m2Km(values):
	distance_ = []
	# convert from m to Km
	for i in range(0, len(values)):
		distance_.append(values[i]/1000)

	return distance_

def Km2m(values):
	distance_ = []
	# convert from Km to m
	for i in range(0, len(values)):
		distance_.append(values[i]*1000)

	return distance_

def B_k(distance, k):
	b_k = []
	x_total = distance[-1]
	for x in distance:
		# print(x)
		b_k.append(0.07849*x*(x_total - x)/k)
	return b_k; 

def B_e(distance):
	b_e = []
	x_total = distance[-1]
	for x in distance:
		# print(x)
		b_e.append(0.07849*x*(x_total - x))
	return b_e; 

def getMax(values):
	print(max(values))

def plot(n, title, distance, elevation):
	plt.figure(n)
	plt.fill_between(distance,0, elevation)
	plt.title(title)
	plt.ylabel('Elevation (m)')
	plt.xlabel('Distance (m)')


if __name__ == "__main__":
	main()