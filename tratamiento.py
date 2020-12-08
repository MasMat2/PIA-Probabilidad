from collections import defaultdict
import math
import valores


datos = valores.datos
datos.sort()

def media(datos):
    return sum(datos)/len(datos)

def mediana(datos):
    datos.sort()
    if(len(datos)%2):
        m = len(datos)//2
        return datos[m]
    else:
        m = len(datos)//2
        return (datos[m-1]+datos[m])/2


def moda(datos):
    frecuencias = defaultdict(int)
    max_f=0
    for i in datos:
        frecuencias[i]+=1
        if frecuencias[i]>max_f:
            max_f = frecuencias[i]
    multi_modas = list(kv for kv in frecuencias.items() if kv[1]==max_f)
    multi_modas.sort(key=lambda kv: kv[0])
    # return dict(sorted(frecuencias.items(), key=lambda kv: kv[1], reverse=True))
    return multi_modas

def rango_medio(datos):
    datos.sort()
    return (datos[0]+datos[-1])/2

def varianza_poblacional(datos):
    numerador = sum(map(lambda i : i * i, datos)) - len(datos)*math.pow(media(datos), 2)
    return numerador/(len(datos))

def varianza_muestral(datos):
    numerador = sum(map(lambda i : i * i, datos)) - len(datos)*math.pow(media(datos), 2)
    return numerador/(len(datos)-1)

def desviacion_estandar_poblacional(datos):
    return math.sqrt(varianza_poblacional(datos))

def desviacion_estandar_muestral(datos):
    return math.sqrt(varianza_muestral(datos))

def desviacion_estandar_aprox(datos):
    datos.sort()
    return (datos[-1]-datos[0])/4

def datos_agrupados(datos):
    datos.sort()
    numero_clases = round(1+math.log(len(datos), 2))
    amplitud_clases = (datos[-1]-datos[0])/numero_clases
    marcas = defaultdict(int)
    for i in range(numero_clases):
        marcas[datos[0]+(i+1/2)*amplitud_clases]
    counter = 0
    for dato in datos:
        if dato>datos[0]+(counter+1)*amplitud_clases:
            counter = min(counter+1, len(list(marcas.keys()))-1)
            marcas[list(marcas.keys())[counter]]+=1
        else:
            marcas[list(marcas.keys())[counter]]+=1
    return marcas

def media_datos_agrupados(datos):
    datos_g = datos_agrupados(datos)
    return sum(map(lambda kv: kv[0]*kv[1], datos_g.items()))/(sum(datos_g.values()))


def varianza_poblacional_datos_agrupados(datos):
    datos_g = datos_agrupados(datos)
    n=sum(datos_g.values())
    numerador= sum(map(lambda kv: math.pow(kv[0],2)*kv[1], datos_g.items()))-n*math.pow(media_datos_agrupados(datos),2)
    return numerador/(n)

def desviacion_estandar_poblacional_datos_agrupados(datos):
    return math.sqrt(varianza_poblacional_datos_agrupados(datos))

def varianza_muestral_datos_agrupados(datos):
    datos_g = datos_agrupados(datos)
    n=sum(datos_g.values())
    numerador= sum(map(lambda kv: math.pow(kv[0],2)*kv[1], datos_g.items()))-n*math.pow(media_datos_agrupados(datos),2)
    return numerador/(n-1)
    
def desviacion_estandar_muestral_datos_agrupados(datos):
    return math.sqrt(varianza_muestral_datos_agrupados(datos))

def coeficiente_de_variacion(datos):
    return desviacion_estandar_muestral(datos)*100/media(datos)

if __name__ == "__main__":
    print(f"{'media':<31} {media(datos)}")
    print(f"{'mediana':<31} {mediana(datos)}")
    print(f"{'moda':<31} {moda(datos)}")
    print(f"{'rango medio':<31} {rango_medio(datos)}")
    print(f"{'desviacion estandar muestral':<31} {desviacion_estandar_muestral(datos)}")
    print(f"{'varianza muestral':<31} {varianza_muestral(datos)}")
    print(f"{'desviacion estandar aproximada':<31} {desviacion_estandar_aprox(datos)}")
    print("\nDatos Agrupados")
    print(f"{'media datos agrupados':<45} {media_datos_agrupados(datos)}")
    print(f"{'varianza muestral datos agrupados':<45} {varianza_muestral_datos_agrupados(datos)}")
    print(f"{'desviacion estandar muestral datos agrupados':<45} {desviacion_estandar_muestral_datos_agrupados(datos)}")
    print(f"{'coeficiente de variacion:':<31} {coeficiente_de_variacion(datos)}%")

    print("\n")
    print(f"{'coeficiente de variacion:':<31} {coeficiente_de_variacion(datos)}%")
    print(f"{'media':<31} {media(datos)}")
    print(f"{'mediana':<31} {mediana(datos)}")
    print(f"{'moda':<31} {moda(datos)}")
    print(f"{'rango medio':<31} {rango_medio(datos)}")
    print(f"{'desviacion estandar poblacional':<31} {desviacion_estandar_poblacional(datos)}")
    print(f"{'varianza poblacional':<31} {varianza_poblacional(datos)}")
    print(f"{'desviacion estandar aproximada':<31} {desviacion_estandar_aprox(datos)}")
    print("\nDatos Agrupados")
    print(f"{'media datos agrupados':<45} {media_datos_agrupados(datos)}")
    print(f"{'varianza poblacional datos agrupados':<45} {varianza_poblacional_datos_agrupados(datos)}")
    print(f"{'desviacion estandar poblacional datos agrupados':<45} {desviacion_estandar_poblacional_datos_agrupados(datos)}")
    print(f"{'coeficiente de variacion:':<31} {coeficiente_de_variacion(datos)}%")