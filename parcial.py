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
d = [0, 0.5, 2.5, 4, 5, 6, 8]
# A en m
A = [1450, 1260, 1100, 1100, 1400, 1450, 1430]
# distancia total
dt = d[-1]
# distancia hasta la 1era repetidora
d1 = 2.3
# distancia desde la repetidora al final
d2 = dt-d1
# potencia de transmision dB
Ptx = utils.dBm2dB(20)
# potencia máxima de recepcion dB
Prx_max = utils.dBm2dB(-70)
# sensibilidad del receptor DB
Srx = utils.dBm2dB(-76)
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
# OJO: longitud de onda en m
lambda_m = c/(f*pow(10, 6))
lambda_Km = utils.m2Km(lambda_m)
# índice troposférico
k = 0.4
# pérdidas por 100 metros de guía de onda
alpha = 29
# Ganancia de la antena dBi
G = 39

# p = profile.calcProfileFullCorrection(d, A, k)
p1 = profile.calcSimpleProfileFullCorrection(d, d1, A, k)
# p2 = profile.calcProfileEarthCorrection(d, A)
# p3 = profile.calProfileRefractionCorrection(d, A, k)

profile.plotProfileArrays(2, d, A, title="Earth")
profile.plotProfileArrays(3, d, p1, title="Corrections")

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
Gt = G
Lt = lg1 + lg2 + 2*lb + ll
Prx = Ptx + Gt - Lt

# Cálculo de Fresnel

pxBaseAntena1 = d[0]         # Km
pyBaseAntena1 = A[0]         # m
hAntena1 = h_t1                # m

pxBaseAntena2   = d[len(d)-1]   # Km
pyBaseAntena2   = A[len(A)-1]   # m
hAntena2 = h_t2                   # m

# Calculo del Haz
(m,b) = fresnel.hazEntreAntenas(pxBaseAntena1, pyBaseAntena1, hAntena1,
                        pxBaseAntena2, pyBaseAntena2, hAntena2)

# Colisiones entre el haz(incluido fresnel) y los obstáculos
(alturaHaz, radioFresnel, deltaH) = fresnel.getRayObstacleDifference(m, b, 1, f*1000,
                              d, A,
                              pxBaseAntena1, pxBaseAntena2)

colision = fresnel.checkColision(deltaH)

printHeader("Colisiones del Haz: ")
printHeader("Calculo de Fresnel entre la antena emisora y receptora: ")
print("Alturas del Haz sobre cada parte del terreno [m]")
print('\t'+str(alturaHaz))
print("Radio de Fresnel sobre cada parte del terreno [m]")
print('\t'+str(radioFresnel))
print("Diferencia entre la altura del haz y la altura del terreno (junto con el radio de Fresnel)")
print('\t'+str(deltaH))
print("Chequeo de colisiones en cada punto del terreno")
print('\t'+str(colision))
for i in range(len(colision)):
    if(colision[i]):
        print('\tColisión en X = '+str(d[i]) + " Km")

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
print("\n\n")

# OJO!!! siempre dejar esto al final para que no se cierren los gráficos
# no importa si no estás graficando
profile.plotShow()
