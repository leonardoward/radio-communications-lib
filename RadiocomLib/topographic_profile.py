import matplotlib.pyplot as plt
import pandas as pd

def main():
	# load data
	data = pd.read_csv('data4.csv')

	distance = data.Distance
	elevation = data.Elevation
	
	distance = distance.tolist()
	elevation = elevation.tolist()

	k = float(input('Índice atmosférico: '))

	distance_ = []
	# convert from m to m
	for i in range(0, len(distance)):
		distance_.append(distance[i]/1000)

	# curvaturas por difracción
	new_elevation = B_k(distance_, k)

	# curvaturas por perturbación terrestre
	new_elevation1 = B_e(distance_)

	final_elevation = []
	
	[final_elevation.append(x + y + z) for x, y, z in zip(elevation, new_elevation, new_elevation1)]

	# without index atmospheric
	# plot(1, 'Topographic Profile', distance, elevation)

	# only with index atmospheric
	# plot(2, 'Topographic Profile (Perturbaciones terrestres)', distance, new_elevation)

	# 04141519508

	# only with index atmospheric
	# plot(3, 'Topographic Profile (Perturbaciones por refracción)', distance, new_elevation1)

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

def findPeaks(values):
	d_values = []

	max = len(values)
	for i in range(0, max):
		if (i != max-1):
			d_values.append(values[i+1]-values[i])




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