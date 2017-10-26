import matplotlib.pyplot as plt
import RadiocomLib
from RadiocomLib import *
from printColors import printHeader, printSubHeader, printWarning, printOK, printFail

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
Ptx = utils.dBm2dB(20)
# potencia máxima de recepción
Prx_max = utils.dBm2dB(-25)
# sensibilidad del receptor
Srx = utils.dBm2dB(-76)
# pérdidas en brach dB/estación
lb = 2 
# altura de la torre emisora
t1 = 90
# altura de las repetidoras
tr1 = 0
# altura de la torre receptora
t2 = 90
# frecuencia en GHz
f = 7
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

lt = lg1 + lg2 + lr1
Prx = Ptx - lt


printHeader("Balance de Pontecia: ")
printSubHeader("\tPerdidas: ")
print("\t\tTotal: "+ str(lt))
print("\t\tWave Guide: "+ str(lg1+lg2))
print("\t\tPassive Repeter: "+ str(lr1))
printSubHeader("\tPotencia: ")
print("\t\tTX: "+str(Ptx))
print("\t\tRX: "+str(Prx) + " MAX: "+str(Prx_max) + " SENSIBILIDAD: " + str(Srx))


# OJO!!! siempre dejar esto al final para que no se cierren los gráficos
# no importa si no estás graficando
profile.plotShow()