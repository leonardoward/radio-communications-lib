import math

def sum(a,b):
    return a + b

# Datos para calcular el radio de Fresnel
f = 12770000
lambda_ = 300000000/f

# Antenas
pxAntena1 = 0
pyAntena1 = 909
hAntena1 = 850
pyAntena1 = pyAntena1 + hAntena1

pxAntena2   = 21605
pyAntena2   = 185
hAntena2 = 850
pyAntena2 = pyAntena2 + hAntena2

# Obstáculos
pxObstacles = [19455, 14556, 7762]
pyObstacles = [468.75, 893.75, 1053.2]

# Ecuación de la recta
m = (pyAntena2 - pyAntena1)/(pxAntena2 - pxAntena1)
b = pyAntena1
print("m = "+str(m))
print("b = "+str(b))
hazPoints = []

for x in range(pxAntena2):
    newY = m*x + b
    for i in range(len(pxObstacles)):
        if(pxObstacles[i] == x):
            rFresnel = math.sqrt((lambda_*x*(pxAntena2-x))/pxAntena2)
            print("x = " + str(x))
            print("Altura del obstaculo = " + str(pyObstacles[i]))
            print("Radio de Fresnel = " + str(rFresnel))
            print("Altura del Haz = " + str(newY))
            deltaH = newY - (pyObstacles[i] + rFresnel)
            print("Altura del Haz - (Altura del obstaculo + radio de Fresnel) = " + str(deltaH))
            if(deltaH < 0):
                print("Error")


    hazPoints.append(newY)
