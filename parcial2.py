import math
import matplotlib.pyplot as plt
from printColors import printHeader, printSubHeader, printWarning, printOK, printFail
from RadiocomLib import *

# ##############################################################################
# ##                            Variables                                     ##
# ##############################################################################
d1 = 8                  # Km
d2 = 30                 # Km
htorrePiritu = 30       # m
hTorreJose = 30         # m
Prx1 = -30              # dBm
Prx2 = -41              # dBm
f1 = 13                 # GHz
f2 = 7                  # GHz
factorClima = [4,4]
f = [f1,f2]
Prx = [Prx1,Prx2]
distancia = [d1, d2]
rugosidadTerreno = [1,1]
# ##############################################################################
# ##                            Cálculos                                      ##
# ##############################################################################

print()
printColors.printSubHeader("Calculos")
print()

b = quality.influenciaTerreno_b(rugosidadTerreno)
print("Influencia del terreno (b)")
print("\tb = "+str(b) + " Nondimensional")
print()

Po = quality.factorAparicionDesvanecimiento_Po(factorClima,b,f,distancia)
print("Factor de Aparición de Desvanecimiento (Po)")
print("\tPo = "+str(Po))
print()

(minBER3, minBER6, tiempoTotalErrores, Pdes3, Pdes6) = quality.condicionesMinimasCalidad(distancia)
print("Objetivo de Calidad para BER 10^⁻3")
print("\tObj Calidad = " + str(minBER3))
print("Objetivo de Calidad para BER 10^⁻6")
print("\tObj Calidad = " + str(minBER6))
print("Probabilidad de que supere una determinada profundidad de desvanecimiento P(F>MF) para BER:10^-3")
print("\tP(F>MF) = " + str(Pdes3))
print("Probabilidad de que supere una determinada profundidad de desvanecimiento P(F>MF) para BER:10^-6")
print("\tP(F>MF) = " + str(Pdes6))
print()

MF3 = quality.margenFailing(Po,Pdes3)
print("Margen de desvanecimiento para BER:10^-3")
print("\tMF-3 = " + str(MF3) + " dB")
print()

MF6 = quality.margenFailing(Po,Pdes6)
print("Margen de desvanecimiento para BER:10^-6")
print("\tMF-6 = " + str(MF6)+ " dB")
print()

Srx3 = quality.sensibilidad(Prx,MF3)
print("Sensibilidad del receptor Srx para BER:10^-3")
print("\tSrx = "+str(Srx3)+ " dBm")
print()

Srx6 = quality.sensibilidad(Prx,MF6)
print("Sensibilidad del receptor Srx para BER:10^-3")
print("\tSrx = "+str(Srx3)+ " dBm")
print()

# índice troposférico
k = 0.4
# velocidad de la luz
c = 3*pow(10, 8)
# d en Km
d = [0, 8, 30]
# A en m
A = [0, 0, 50]
# distancia total
dt = d[-1]
# distancia hasta la 1era repetidora
d1 = 8
# distancia desde la repetidora al final
d2 = dt-d1

# pérdidas en brach dB/estación
lb = 2
# altura de la torre emisora
h_t1 = 40
# altura de las repetidoras
h_tr1 = 0
# altura de la torre receptora
h_t2 = 80
# frecuencia en GHz
f = 21

# p = profile.calcProfileFullCorrection(d, A, k)
p1 = profile.calcSimpleProfileFullCorrection(d, d1, A, k)
# p2 = profile.calcProfileEarthCorrection(d, A)
# p3 = profile.calProfileRefractionCorrection(d, A, k)

print(utils.dBm2dB(-41))
print(utils.dBm2dB(-30))

I = (0.8/(7*30))*2*math.pow(10,15.3317/10)
print(I)
