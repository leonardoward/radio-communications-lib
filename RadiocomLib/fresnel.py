import math
import matplotlib.pyplot as plt

def fresnelRadius(n, d1, d2, f):
    # Rn = radio de la n-sima zona de fresnel (m)
    # f  = frecuencia (MHz)
    # d1 = distancia del transmisor al plano considerado (Km)
    # d2 = distancia del plano considerado al receptor (Km)
    Rn = 548*math.sqrt((n*d1*d2)/(f*(d1+d2)))
    return Rn

def hazEntreAntenas(pxBaseAntena1, pyBaseAntena1, hAntena1,
                    pxBaseAntena2, pyBaseAntena2, hAntena2):
    # pxBaseAntena1 -> km
    # pxBaseAntena2 -> km
    # pyBaseAntena1 -> m
    # pyBaseAntena2 -> m
    # hAntena1 -> m
    # hAntena2 -> m
    # Ecuación de la recta
    m = ((pyBaseAntena2+hAntena2) - (pyBaseAntena1+hAntena1))/(pxBaseAntena2-pxBaseAntena1)
    b = ((pyBaseAntena1+hAntena1) + (pyBaseAntena2+hAntena2) - m*(pxBaseAntena1+pxBaseAntena2))/2
    return (m,b)

def getRayObstacleDifference(m, b, n, f, pxObstacles, pyObstacles, pxBaseAntena1, pxBaseAntena2):
    # m -> pendiente de la ecuación de la recta del haz
    # b -> punto de corte del eje Y de la ecuación de la recta del haz [m]
    # n -> Número de radios de Fresnel
    # pxObstacles -> Arreglo con los puntos a evaluar del terreno X [Km]
    # pyObstacles -> Arreglo con los puntos a evaluar del terreno Y [m]

    deltaH = []         # Distancia entre el haz y (obstáculo + radio de fresnel) [m]
    rFresnelArray = []  # Radio de fresnel para cada obstáculo [m]
    alturaHazArray = [] # Altura del haz sobre el obstáculo [m]
    for i in range(len(pxObstacles)):
        hazArray = m*pxObstacles[i] + b
        alturaHazArray.append(hazArray)
        rFresnel = fresnelRadius(n, pxObstacles[i] - pxBaseAntena1, pxBaseAntena2-pxObstacles[i], f)
        rFresnelArray.append(rFresnel)
        deltaH.append(hazArray - (pyObstacles[i] + rFresnel))
    return (alturaHazArray, rFresnelArray, deltaH)

def checkColision(deltaH):
    result = [] # Arreglo con la detección para cada obstáculo, true/false para indicar si colisiona
    for i in range(len(deltaH)):
        if(deltaH[i]<0):
            result.append(True)
        else:
            result.append(False)
    return result

def test():
    f = 12.770000            # MHz
    # Antenas
    pxBaseAntena1 = 0        # Km
    pyBaseAntena1 = 909      # m
    hAntena1 = 700           # m

    pxBaseAntena2   = 21.605  # Km
    pyBaseAntena2   = 185     # m
    hAntena2 = 850            # m

    # Obstáculos
    d = [0, 0.5, 1, 1.8, 2.3, 2.6, 3, 5, 7, 37, 37.5]
    A = [25, 75, 100, 210, 250, 170, 125, 20, 0, 0, 25]
    pxObstacles = [19.455, 14.556, 7.762]          # km
    pyObstacles = [468.75, 893.75, 1053.2]         # m

    # Calculo del Haz

    (m,b) = hazEntreAntenas(pxBaseAntena1, pyBaseAntena1, hAntena1,
                            pxBaseAntena2, pyBaseAntena2, hAntena2)

    # Colisiones entre el haz(incluido fresnel) y los obstáculos
    (alturaHaz, radioFresnel, deltaH) = getRayObstacleDifference(m, b, 1, f,
                                  pxObstacles, pyObstacles,
                                  pxBaseAntena1, pxBaseAntena2)

    colision = checkColision(deltaH)

    print("X Obstáculos [Km]")
    print('\t'+str(pxObstacles))
    print("Y Obstáculos [m]")
    print('\t'+str(pyObstacles))
    print("Alturas del Haz sobre los obstáculos [m]")
    print('\t'+str(alturaHaz))
    print("Radio de Fresnel sobre cada obstáculo [m]")
    print('\t'+str(radioFresnel))
    print("Diferencia entre la altura del haz y la altura del obstáculo (junto con el radio de Fresnel)")
    print('\t'+str(deltaH))
    print("Chequeo de colisiones en cada obstáculo")
    print('\t'+str(colision))
    for i in range(len(colision)):
        if(colision[i]):
            print('\tColisión en X = '+str(pxObstacles[i]) + " Km")

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
