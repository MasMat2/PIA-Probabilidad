from collections import defaultdict
import math
import valores


datos = valores.datos
datos.sort()
#media
def media(datos):
    return sum(datos)/len(datos)

#mediana
def mediana(datos):
    datos.sort()
    if(len(datos)%2):
        m = len(datos)//2
        return datos[m]
    else:
        m = len(datos)//2
        return (datos[m-1]+datos[m])/2

#moda
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

#rango medio
def rango_medio(datos):
    datos.sort()
    return (datos[0]+datos[-1])/2


if __name__ == "__main__":
    print(f"{'media':<31} {media(datos)}")
    print(f"{'mediana':<31} {mediana(datos)}")
    print(f"{'moda':<31} {moda(datos)}")
    print(f"{'rango medio':<31} {rango_medio(datos)}")
