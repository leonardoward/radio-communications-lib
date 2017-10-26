import math
c = 3*pow(10,8) # m/s

def gainAnntena(K, d, f):
    # d = diámetro (m)
    # K = factor de rendimiento (adimensional) [0,5 a 0,7]
    # f = frecuencia Hz
    gainW = (K * math.pow(math.pi,2) * math.pow(d,2))/math.pow(c/f,2)
    gaindB = 10*math.log10(gainW)
    return (gainW, gaindB)

def superficieGeometrica(d):
    # d = diámetro (m)
    sGeometrica = (math.pi * pow(d,2))/4
    return sGeometrica

def superficieEquivalente(K, sGeometrica):
    sEquivalente = K * sGeometrica
    return sEquivalente

def factorRendimiento(sGeometrica, sEquivalente):
    # K = factor de rendimiento (adimensional) [0,5 a 0,7]
    K = sEquivalente/sGeometrica
    return K

def testGain():
    # Ejemplo de la página 4.9 de la guía 2003
    K = 0.65
    d = 1.8
    f = 6*pow(10,9)
    (gainW, gaindB) = gainAnntena(K, d, f)
    print("Ganancia de la antena Parabólica")
    print(str(gainW) + " W")
    print(str(gaindB) + " dBi")
