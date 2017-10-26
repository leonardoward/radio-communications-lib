import matplotlib.pyplot as plt
import RadiocomLib
from RadiocomLib import *
import printColors

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
k = 0.4
alpha = 2.4
t1 = 90
tr1 = 0
t2 = 90
dt = 37.5
d1 = 2.6
d2 = dt-d1
pt = 20


p = profile.calcProfileFullCorrection(d, A, k)
# p1 = profile.calcProfileEarthCorrection(d, A)
# p2 = profile.calProfileRefractionCorrection(d, A, k)

profile.plotProfileArrays(2, d, A, title="Earth")
profile.plotProfileArrays(3, d, p, title="Corrections")

ls1 = losses.waveGuide(alpha, t1)
ls2 = losses.waveGuide(alpha, t2)
# print(ls1)
ls3 = losses.passiveRepeter(f, d1, d2)



# OJO!!! siempre dejar esto al final para que no se cierren los gráficos
# no importa si no estás graficando
profile.plotShow()
