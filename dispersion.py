from collections import defaultdict
import math
import valores


datos = valores.datos
datos.sort()
#media
def media(datos):
    return sum(datos)/len(datos)

#varianza poblacional
def varianza_poblacional(datos):
    # numerador = sum(map(lambda i : i * i, datos))/(len(datos)) - math.pow(media(datos), 2)
    numerador = sum(map(lambda i : i * i, datos)) - len(datos)*math.pow(media(datos), 2)
    med = media(datos)
    # numerador = sum(map(lambda xi: math.pow(xi-med, 2), datos))
    return numerador/len(datos)

#desviacion estandar poblacional
def desviacion_estandar_poblacional(datos):
    return math.sqrt(varianza_poblacional(datos))

#varianza muestral
def varianza_muestral(datos):
    # numerador = sum(map(lambda i : i * i, datos)) - len(datos)*math.pow(media(datos), 2)
    return numerador/(len(datos)-1)

#desviacion estandar
def desviacion_estandar_muestral(datos):
    return math.sqrt(varianza_muestral(datos))

#rango/4 Aproximada desviacion estandar
def rango4(datos):
    return (datos[-1]-datos[0])/4

if __name__ == "__main__":
    print(f"{'varianza poblacional':<31} {varianza_poblacional(datos)}")
    print(f"{'desviacion estandar poblacional':<31} {desviacion_estandar_poblacional(datos)}")
    print(f"{'desviacion estandar aproximada':<31} {rango4(datos)}")