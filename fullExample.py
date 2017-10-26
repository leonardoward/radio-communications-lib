import matplotlib.pyplot as plt
import RadiocomLib
from RadiocomLib import *
from printColors import printHeader, printSubHeader, printWarning, printOK, printFail
from math import pow

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

# velocidad de la luz
c = 3*pow(10, 8)
# d en Km
d = [0, 0.5, 1, 1.8, 2.3, 2.6, 3, 5, 7, 37, 37.5]
# A en m
A = [25, 75, 100, 210, 250, 170, 125, 20, 0, 0, 25]
# distancia total
dt = d[-1]
# distancia hasta la 1era repetidora
d1 = 2.3
# distancia desde la repetidora al final
d2 = dt-d1
# potencia de transmision dB
Ptx = utils.dBm2dB(20)
# potencia máxima de recepcion dB
Prx_max = utils.dBm2dB(-25)
# sensibilidad del receptor DB
Srx = utils.dBm2dB(-76) 
# pérdidas en brach dB/estación
lb = 2
# altura de la torre emisora
h_t1 = 90
# altura de las repetidoras
h_tr1 = 0
# altura de la torre receptora
h_t2 = 90
# frecuencia en GHz
f = 7
# OJO: longitud de onda en m
lambda_m = c/(f*pow(10, 6))
lambda_Km = utils.m2Km(lambda_m)
# índice troposférico
k = 0.4
# pérdidas por 100 metros de guía de onda
alpha = 2.4
# Ganancia de la antena dBi
G = 31

p = profile.calcProfileFullCorrection(d, A, k)
# p1 = profile.calcProfileEarthCorrection(d, A)
# p2 = profile.calProfileRefractionCorrection(d, A, k)

# profile.plotProfileArrays(2, d, A, title="Earth")
# profile.plotProfileArrays(3, d, p, title="Corrections")

# perdidas por guía de onda

lg1 = losses.waveGuide(alpha, h_t1)
lg2 = losses.waveGuide(alpha, h_t2)

# pérdidas en trasmisor pasivo

lr1 = losses.passiveRepeter(f, d1, d2)

# pérdidas por lluvia dB
ll = losses.lluvia(1.4, dt)

# potencia recibida dB
Pr1 = power.powerReceive(lambda_Km, Ptx, G, G, d1)

# Ganancia total de todas las antenas
Gt = G + G + G + G
Lt = lg1 + lg2 + lr1 + 2*lb + ll
Prx = Ptx + Gt - Lt

printHeader("Balance de Pontecia: ")
printSubHeader("\tPerdidas: ")
print("\t\tTotal: "+ str(Lt) + " dB")
print("\t\tWave Guide: "+ str(lg1+lg2) + " dB")
print("\t\tPassive Repeter: "+ str(lr1) + " dB")
print("\t\tPérdidas por lluvia: "+ str(ll) + " dB")
print("\t\tPérdidas por branch: "+ str(lb) + " dB")
printSubHeader("\tPotencia: ")
print("\t\tGanancia totales: "+str(Gt) + " dB")
print("\t\tTx: "+str(Ptx) + " dB")
print("\t\tRx: "+str(Prx) + "\t\tMAX: "+str(Prx_max) + "\tSENSIBILIDAD: " + str(Srx) + " dB")


# OJO!!! siempre dejar esto al final para que no se cierren los gráficos
# no importa si no estás graficando
profile.plotShow()