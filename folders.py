#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from reportlab.pdfgen import canvas


#Leer lista a imprimir

reporte = list(csv.reader(open("QA03.csv")))#se lee el archivo csv de Reporte Diario y se carga en lista
sud = []
fecha = raw_input("Introduce la fecha de los documentos en formato (dd/mm/aaaa): ")
centro = raw_input("Introduce el centro que deseas imprimir: ")
reporte_filtrado = []
contador = 0

for row in reporte[1:]:
	if row[0] == fecha and row[1] == centro:
		reporte_filtrado.append(row)
		contador = contador +1

print contador	

#Asignar el numero de caja

cajas = list(csv.reader(open("Cajas.csv"))) 

lista_impresion = []
for row in reporte_filtrado:
	nutra = int(row[2])
	nombre = row[3]
	paterno = row[4]
	materno = row[5]
	
	for box in cajas[1:]:
		lista_folders = []
		nutra_inicial = int(box[1])
		nutra_final = int(box[2])
		if nutra >= nutra_inicial and nutra <= nutra_final:
			no_de_caja = box[0]
			lista_folders.append(str(nutra))
			lista_folders.append(nombre)
			lista_folders.append(paterno)
			lista_folders.append(materno)
			lista_folders.append(no_de_caja)
			lista_impresion.append(lista_folders)

		
print lista_impresion[0]
print lista_impresion[210]
#Mandar a hoja de impresiòn


aux = canvas.Canvas("folders.pdf")

for registro in lista_impresion:
	
	a = str(registro[0]) #Nutra y Nombre
	print a
	b = str(registro[1])
	print b
	c = str(registro[2])
	d = str(registro[3])
	e = str(registro[4])
	
	nombre_imp = a, "     ",d," ",c, ", ",b
	caja_imp = e
	print nombre_imp.decode(utf8)
	aux.setPageSize((839.055, 1303.94))#defino el tamaño de papel
	
	aux.setFillColor('grey')
	aux.setFont('Helvetica', 35)
	aux.drawString(45,350, nombre_imp.decode('utf8'))
					
		
	aux.setLineWidth(8)
	aux.setStrokeColor("grey")
	aux.roundRect(10,10,592,297,5,stroke=1,fill=0)
	aux.setFillColor("black")#defino el color de la fuente
	aux.setFont('Helvetica', 200)#defino tipografia y tamaño
	aux.drawCentredString(420,120, caja_imp)#dibujo el texto de numero de caja
	aux.setFillColor("black")#defino el color de la fuente
	aux.setFont('Helvetica', 50)#defino tipografia y tamaño
	aux.drawCentredString(306,35, nombre_imp.decode('utf8'))#dibujo el texto
	aux.showPage()

aux.save()
