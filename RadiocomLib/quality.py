import math

# ##############################################################################
# ##                        Influencia de Terreno b                           ##
# ##############################################################################

def influenciaTerreno_b(rugosidad):
    # rugosidad (s)             ->      Nondimensional
    b = []
    for i in range(len(rugosidad)):
        b.append(math.pow(rugosidad[i]/15,-1.3))
    return b

# ##############################################################################
# ##                        Factor de desvanecimiento Po                      ##
# ##############################################################################

def factorAparicionDesvanecimiento_Po (factorClima, influenciaTerreno, frequency, distancia):
    # factorClima (a)           ->      Nondimensional
    # influenciaTerreno (b)     ->      Nondimensional
    # frequency (f)             ->      GHz
    # distancia (d)             ->      Km
    Po = []
    for i in range(len(distancia)):
        Po.append(0.3 * factorClima[i] * influenciaTerreno[i] * (frequency[i]/4) * math.pow(distancia[i]/50,3))
    return Po

# ##############################################################################
# ##         Condiciones Mínimas de Calidad BER:10^-3 BER:10^-6               ##
# ##############################################################################

def condicionesMinimasCalidad(distancia):   # distancia <= 2500
    minBER3 = []
    minBER6 = []
    tiempoTotalErrores = []
    Pdes3 = []
    Pdes6 = []
    for i in range(len(distancia)):
        # distancia (L)              ->      Km
        if(distancia[i] <= 280): distancia[i] = 280
        if(distancia[i] >= 2500): print("Error in distance = "+str(distancia[i]))
        # 1·10^-3   durante más del 0,054% de cualquier mes; con tiempo de integración
        #           de un segundo
        minBER3.append((distancia[i] * 0.054)/2500)  # BER^-3 (%)
        # 1·10^-6   durante más del 0,4% de cualquier mes; con tiempo de integración de un
        #           minuto. Esta cota también tiene como límite no excederse de BER = 10-3; es decir,
        #           durante el 0,4% del tiempo, la tasa de error debe estar comprendida entre 10-6 y 10-3.
        minBER6.append((distancia[i] * 0.4)/2500)    # BER^-6 (%)
        # El tiempo total de segundos con errores no debe exceder 0,32% de cualquier mes
        tiempoTotalErrores.append((distancia[i] * 0.32)/2500)
    for i in range(len(minBER3)):
        Pdes3.append(minBER3[i]/100)
        Pdes6.append(minBER6[i]/100)
    return  (minBER3,minBER6,tiempoTotalErrores,Pdes3,Pdes6)

def margenFailing(factorAparicionDesvanecimiento, probabilidadSupereProfDesvanecimiento):
    MF = []
    for i in range(len(factorAparicionDesvanecimiento)):
        MF.append(-10*math.log10(probabilidadSupereProfDesvanecimiento[i]/factorAparicionDesvanecimiento[i]))
    return MF

def sensibilidad(potenciaReceptor, margenDesvanecimiento):
    Srx = []
    for i in range(len(potenciaReceptor)):
        Srx.append(potenciaReceptor[i] - margenDesvanecimiento[i])
    return Srx
