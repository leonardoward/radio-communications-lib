import math

def sum(a,b):
    return a + b

def fresnelRadius(n, d1, d2, f):
    # Rn = radio de la n-sima zona de fresnel (m)
    # f  = frecuencia (MHz)
    # d1 = distancia del transmisor al plano considerado (km)
    # d2 = distancia del plano considerado al receptor (km)
    Rn = 548*math.sqrt((n*d1*d2)/(f*(d1+d2)))
    return Rn

def hazEntreAntenas(pyBaseAntena1, hAntena1
                    pyBaseAntena2, hAntena2
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
        hazX.append(newY)
        hazY.append(newY)
    return (hazX,hazY)

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
