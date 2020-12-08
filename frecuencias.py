import valores
import tratamiento
import xlsxwriter
import math

datos = valores.datos
datos.sort()

marcas = tratamiento.datos_agrupados(datos)
amplitud = list(marcas.keys())[1]-list(marcas.keys())[0]

counter = 0
workbook = xlsxwriter.Workbook('Tabla de frecuencias.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write("A1", "i")
worksheet.write("B1", "Intervalos de clase")
worksheet.write("C1", "Frecuencia:fi")
worksheet.write("D1", "Frecuencia relativa = proporcion")
worksheet.write("E1", "Porcentaje")
worksheet.write("F1", "Frecuencia acumulada")
worksheet.write("G1", "Marca de clase:mi")
worksheet.write("H1", "fi*mi")
worksheet.write("I1", "mi2")
worksheet.write("J1", "fi*mi2")
worksheet.write_column('A2', [i for i in range(1,len(marcas.keys())+1)])
worksheet.write_column('B2', [f"{datos[0]+i*amplitud:.4} - {datos[0]+(i+1)*amplitud:.4}" for i in range(len(marcas.keys()))])
worksheet.write_column('C2', marcas.values())
worksheet.write_column('D2', [f"{i/(sum(marcas.values())):.4}" for i in marcas.values()])
worksheet.write_column('E2', [f"{(i/sum(marcas.values()))*100:.4}%" for i in marcas.values()])
worksheet.write_column('F2', [counter:=counter+i for i in marcas.values()])
worksheet.write_column('G2', [f"{i:0.2f}" for i in marcas.keys()])
worksheet.write_column('H2', [f"{i:0.2f}" for i in map(lambda kv: kv[0]*kv[1], marcas.items())])
worksheet.write_column('I2', [f"{i:0.2f}" for i in map(lambda x: math.pow(x, 2), marcas.keys())])
worksheet.write_column('J2', [f"{i:0.2f}" for i in map(lambda kv: math.pow(kv[0],2)*kv[1], marcas.items())])
print(marcas.items())
print(list(map(lambda kv: math.pow(kv[0],2)*kv[1], marcas.items())))

workbook.close()
