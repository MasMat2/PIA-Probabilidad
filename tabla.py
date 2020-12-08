import valores
import xlsxwriter
import math

datos = valores.datos

workbook = xlsxwriter.Workbook('tabla.xlsx')
worksheet = workbook.add_worksheet()
for i in range(18):
    row = f"{chr(ord('A')+i)}"
    for j in range(8):
        column = f"{chr(ord('A')+j)}"
        worksheet.write(f"{column}{i+1}", datos[i*8+j])
workbook.close()

