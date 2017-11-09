import math
import matplotlib.pyplot as plt
from printColors import printHeader, printSubHeader, printWarning, printOK, printFail
from RadiocomLib import *

# ##############################################################################
# ##                        Enunciado Ejercicio 1                             ##
# ##############################################################################

enunciado = """
1. En un proceso de licitación para contratar la instalación llave en mano de un enlace de
microondas en la banda de 21 GHz entre Sartenejas y Los Palos Grandes (8 km), con un
repetidor pasivo en El Volcán, se presentan cuatro empresas a concurso.
El enlace será de baja capacidad (E2). Considere una rugosidad del terreno s=40
b) Determine las condiciones mínimas para el cumplimiento del objetivo de calidad de
   la UIT (BER=10-3).Presente todos los cálculos e indique la empresa a recomendar.
"""

printColors.printWarning(enunciado)

# ##############################################################################
# ##                            Variables                                     ##
# ##############################################################################

print()
printColors.printSubHeader("Datos")
print()

f = [21]                 # Frequency GHz
distancia = [8]          # Km
rugosidadTerreno = [40]  # Nondimensional
factorClima = [4]

print("\tFrecuencia = "+str(f) + " GHz")
print("\tDistancia = "+str(distancia) + " Km")
print("\tRugosidad Terreno = "+str(rugosidadTerreno) + " Nondimensional")
print("\tFactor Clima = "+str(factorClima) + " Nondimensional")

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

# ##############################################################################
# ##                        Enunciado Ejercicio 2                             ##
# ##############################################################################

enunciado = """
2.Se diseña un enlace entre Caraballeda y Tacoa en la banda de 13 GHz, que requiere
un repetidor activo en Catia La Mar (capacidad de trafico: E3)
Se utiliza diversidad de espacio en el salto Catia La Mar-Tacoa porque el punto de
reflexión ocurre sobre el mar, independientemente de la altura seleccionada para las
antenas en las torres disponibles, y se prevé la aparición de reflexiones frecuentes. Se
obtiene una mejora (I) de valor 10. Evalúe las sensibilidades mínimas requeridas para
satisfacer los objetivos de calidad (BER:10-3 y BER: 10-6). Se impone como condición que
los transceptores utilizados en ambos vanos sean los mismos.
"""

printColors.printWarning(enunciado)

# ##############################################################################
# ##                            Variables                                     ##
# ##############################################################################

print()
printColors.printSubHeader("Datos")
print()

f = [13,13]                 # Frequency GHz
I = 10                      # Improvement Nondimensional
distancia = [12,8]          # Km
rugosidadTerreno = [10,5]   # Nondimensional
Prx = [-60,-55]             # dBm
factorClima = [4,4]

print("\tFrecuencia = "+str(f) + " GHz")
print("\tDistancia = "+str(distancia) + " Km")
print("\tRugosidad Terreno = "+str(rugosidadTerreno) + " Nondimensional")
print("\tPotencia Recibida = "+str(Prx) + " dBm")
print("\tFactor Clima = "+str(factorClima) + " Nondimensional")

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
