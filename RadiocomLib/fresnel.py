import math
import matplotlib.pyplot as plt

def fresnelRadius(n, d1, d2, f):
    # Rn = radio de la n-sima zona de fresnel (m)
    # f  = frecuencia (Hz)
    # d1 = distancia del transmisor al plano considerado (m)
    # d2 = distancia del plano considerado al receptor (m)
    f = f/1000000   # Hz -> MHz
    d1 = d1/1000    # m -> Km
    d2 = d2/1000    # m -> Km
    Rn = 548*math.sqrt((n*d1*d2)/(f*(d1+d2)))
    return Rn

def hazEntreAntenas(pyBaseAntena1, hAntena1,
                    pyBaseAntena2, hAntena2,
                    distEntreAntenas):

    # Ecuación de la recta
    m = ((pyBaseAntena2+hAntena2) - (pyBaseAntena1+hAntena1))/distEntreAntenas
    b = (pyBaseAntena1+hAntena1)
    # print("m = "+str(m))
    # print("b = "+str(b))
    hazX = []
    hazY = []
    for x in range(distEntreAntenas):
        newY = m*x + b
        hazX.append(x)
        hazY.append(newY)
    return (hazX,hazY)

def checkColisionFresnel(hazX, hazY, n, f, pxObstacles, pyObstacles, distEntreAntenas):
    deltaH = []        # Distancia entre el haz y (obstáculo + radio de fresnel)
    radioFresnel = []  # Radio de fresnel para cada obstáculo
    alturaHazObstaculo = [] #Altura del haz sobre el obstáculo
    for x in range(len(hazX)):
        for i in range(len(pxObstacles)):
            if(pxObstacles[i] == x):
                rFresnel = fresnelRadius(n, x, distEntreAntenas-x, f)
                radioFresnel.append(rFresnel)
                alturaHazObstaculo.append(hazY[i])
                deltaH.append(hazY[i] - (pyObstacles[i] + rFresnel))
                # print("x = " + str(x))
                # print("Altura del obstaculo = " + str(pyObstacles[i]))
                # print("Radio de Fresnel = " + str(rFresnel))
                # print("Altura del Haz = " + str(hazY[x]))
                # print("Altura del Haz - (Altura del obstaculo + radio de Fresnel) = " + str(deltaH))
    return (alturaHazObstaculo, radioFresnel, deltaH)

def test():
    f = 12770000             # Hz
    # Antenas
    pxBaseAntena1 = 0        # m
    pyBaseAntena1 = 909      # m
    hAntena1 = 850           # m

    pxBaseAntena2   = 21605  # m
    pyBaseAntena2   = 185    # m
    hAntena2 = 850           # m

    # Obstáculos
    pxObstacles = [19455, 14556, 7762]             # km
    pyObstacles = [468.75, 893.75, 1053.2]         # m

    # Calculo del Haz

    (hazX,hazY) = hazEntreAntenas(pyBaseAntena1, hAntena1,
                                  pyBaseAntena2,hAntena2,
                                  pxBaseAntena2-pxBaseAntena1)

    # Colisiones entre el haz(incluido fresnel) y los obstáculos
    (alturaHazObstaculo, radioFresnel, deltaH) = checkColisionFresnel(hazX,
                                  hazY, 1, f, pxObstacles, pyObstacles,
                                  pxBaseAntena2-pxBaseAntena1)

    print("Distancia entre cada obstáculo y el haz (sumando el radio de fresnel al obstáculo)")
    print(deltaH)
    plt.plot(hazX, hazY)
    plt.show()

# Datos para calcular el radio de Fresnel
# f = 12770000
# lambda_ = 300000000/f
#
# # Antenas
# pxAntena1 = 0
# pyAntena1 = 909
# hAntena1 = 850
# pyAntena1 = pyAntena1 + hAntena1
#
# pxAntena2   = 21605
# pyAntena2   = 185
# hAntena2 = 850
# pyAntena2 = pyAntena2 + hAntena2
#
# # Obstáculos
# pxObstacles = [19455, 14556, 7762]
# pyObstacles = [468.75, 893.75, 1053.2]
#
# # Ecuación de la recta
# m = (pyAntena2 - pyAntena1)/(pxAntena2 - pxAntena1)
# b = pyAntena1
# print("m = "+str(m))
# print("b = "+str(b))
# hazPoints = []
#
# for x in range(pxAntena2):
#     newY = m*x + b
#     for i in range(len(pxObstacles)):
#         if(pxObstacles[i] == x):
#             rFresnel = math.sqrt((lambda_*x*(pxAntena2-x))/pxAntena2)
#             print("x = " + str(x))
#             print("Altura del obstaculo = " + str(pyObstacles[i]))
#             print("Radio de Fresnel = " + str(rFresnel))
#             print("Altura del Haz = " + str(newY))
#             deltaH = newY - (pyObstacles[i] + rFresnel)
#             print("Altura del Haz - (Altura del obstaculo + radio de Fresnel) = " + str(deltaH))
#             if(deltaH < 0):
#                 print("Error")
#
#
#     hazPoints.append(newY)
