import math


# velocidad de la luz
c = 3*pow(10, 8)
# d en Km
d = [0, 0.5, 1.5, 1.8, 2.5, 3, 4, 8, 8.5]
# A en m
A = [900, 850, 700, 750, 675, 650, 600, 600, 650]
# distancia total
dt = d[-1]
# altura de la torre emisora
h_t1 = 1
# altura de las repetidoras
h_tr1 = 0
# altura de la torre receptora
h_t2 = 1

f = 15*1000000000           # Frecuencia Hz
# Ángulo de Reflexión
beta = 1
       
R = 1
# índice troposférico
k = 0.45


# Diferencia de Recorrido
TPR = math.sqrt(math.pow(dt,2)+math.pow(ht+hr,2))
TR = math.sqrt(math.pow(dt,2)+math.pow(ht-hr,2))
deltaL = TPR - TR

# Diferencia de fase (rad)
lambda_ = c/f
deltaPhase = (4*math.pi*ht*hr)/(lambda_*dt)

# Pérdidas por reflexion
Lrfx = -10*math.log10(1+math.pow(math.abs(R),2)+2*math.abs(R)*math.cos(beta+deltaPhase))
