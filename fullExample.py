import matplotlib.pyplot as plt
import RadiocomLib
from RadiocomLib import *

#------------------------------------------------
# topographic profile
#------------------------------------------------
# calcProfileEarthCorrection(distance, elevation)
# calProfileRefractionCorrection(distance, elevation, k)
# calcProfileFullCorrection(distance, elevation, k)
# plotProfileArrays(distance, elevation)
# Km2m(values)
# m2Km(values)

#------------------------------------------------
# losses
#------------------------------------------------

#------------------------------------------------
# diffraction
#------------------------------------------------

#------------------------------------------------
# fresnel
#------------------------------------------------

# fresnel.test()

d = [0, 0.5, 1, 1.8, 2.3, 2.6, 3, 5, 7, 37, 37.5]
A = [25, 75, 100, 210, 250, 170, 125, 20, 0, 0, 25]
dt = d[-1]
# distancia hasta la 1era repetidora
d1 = 2.6
# distancia desde la repetidora al final
d2 = dt-d1
# potencia de transmisión
pt = 20
# pérdidas en brach dB/estación
lb = 2 
# altura de la torre emisora
t1 = 90
# altura de las repetidoras
tr1 = 0
# altura de la torre receptora
t2 = 90
# frequency
f = 7 # GHz
# índice troposférico
k = 0.4
# pérdidas por 100 metros de guía de onda
alpha = 2.4


p = profile.calcProfileFullCorrection(d, A, k)
# p1 = profile.calcProfileEarthCorrection(d, A)
# p2 = profile.calProfileRefractionCorrection(d, A, k)

# profile.plotProfileArrays(2, d, A, title="Earth")
# profile.plotProfileArrays(3, d, p, title="Corrections")

lg1 = losses.waveGuide(alpha, t1)
lg2 = losses.waveGuide(alpha, t2)
# print(ls1)
lr1 = losses.passiveRepeter(f, d1, d2)



# OJO!!! siempre dejar esto al final para que no se cierren los gráficos
# no importa si no estás graficando
profile.plotShow()