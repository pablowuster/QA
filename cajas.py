#!/usr/bin/env python
# -*- coding: cp1252 -*-

import csv
#calculo el numero de cajas
from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import code39

lista = []
with open ("Jubilados.csv", 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		#if row[7] == "1":
			lista.append(row[0])
		
#lista.sort(reverse=True)
tipo = int(raw_input("Elige que tipo de caja deseas\n	1.Archivo en proceso\n	2.Caja de Archivo entregable\n\nEscribe el número de la opción deseada: "))

exp_por_caja = int(raw_input("Cuantos expedientes quieres guardar en cada caja: "))

no_de_cajas = len(lista) / exp_por_caja
ultima_caja = len(lista) % exp_por_caja
total_exp = len(lista)
total_cajas = no_de_cajas + 1



print "Se hara uso de %d cajas con %d expedientes cada una. En total %d expedientes." %(total_cajas, exp_por_caja, total_exp)
print "La última caja contendrá %d expedientes." %(ultima_caja)
contador = 0
caja = 0
lista_caja_nutra = [["caja","exp_inicial","exp_final"]]

while caja != no_de_cajas:
	fila_caja_nutra = []
	caja += 1
	fila_caja_nutra.append(caja)
	contador += 1
	exp_inicial = lista[contador-1]
	fila_caja_nutra.append(exp_inicial)
	contador += (exp_por_caja - 1) 
	exp_final = lista[contador -1]
	fila_caja_nutra.append(exp_final)
	lista_caja_nutra.append(fila_caja_nutra)
	ultimo_contador = contador

ultima_lista = []
ultima_lista.append(total_cajas)
primer_estribo = total_exp - ultima_caja + 1
ultima_lista.append(lista[primer_estribo])
ultima_lista.append(lista[total_exp-1])
lista_caja_nutra.append(ultima_lista)


with open ("Cajas.csv", 'w') as archivo:
	writer = csv.writer(archivo)
	writer.writerows(lista_caja_nutra)
	



if tipo == 1:

	aux = canvas.Canvas("etiquetas_cajas.pdf")

	for e in lista_caja_nutra[1:]:
	
		a = str(e[0])
		b = str(e[1] + " - "+ e[2])
		barcode_val = "caja_"+a
	
		aux.setPageSize((612, 396))#defino el tamaño de papel
		barcode =code39.Extended39(barcode_val)
		barcode.drawOn(aux,400,350)
		
		aux.setFillColor('grey')
		aux.setFont('Helvetica', 35)
		aux.drawString(45,350, "Supervivencia")
					
		#aux.setFillColor("grey")#defino el color del circulo
		#aux.circle(163,250,130,stroke = 0, fill = 1)#dibujo el circulo
		aux.setLineWidth(8)
		aux.setStrokeColor("grey")
		aux.roundRect(10,10,592,297,5,stroke=1,fill=0)
		aux.setFillColor("black")#defino el color de la fuente
		aux.setFont('Helvetica', 200)#defino tipografia y tamaño
		aux.drawCentredString(420,120, a)#dibujo el texto de numero de caja
		aux.setFillColor("black")#defino el color de la fuente
		aux.setFont('Helvetica', 50)#defino tipografia y tamaño
		aux.drawCentredString(306,35, b)#dibujo el texto
		aux.showPage()

	aux.save()

elif tipo == 2:
	from reportlab.pdfgen import canvas
	from reportlab.lib.colors import PCMYKColor

	sae_blue = PCMYKColor(62,3.5,23,38)
	navy_blue = PCMYKColor(98,5,0,70)

	titulo = raw_input("Ingresa el título: ")
	subtitulo = raw_input("Ingresa el subtitulo")

	aux = canvas.Canvas("cajas_entregable.pdf")
	
	for e in lista_caja_nutra[1:]:
		a = str(e[0])
		b = str(e[1] + " - "+ e[2])
		c = str(total_cajas)
		
		aux.setPageSize((1184, 752))#defino el tamaño de papel

		#MARCAS DE CORTE
		aux.setStrokeColor('Black')
		aux.line(0,0,20,0)#inferior izq
		aux.line(0,0,0,20)
		aux.line(0,752,20,752)#superior izq
		aux.line(0,752,0,732)
		aux.line(1184,0,1184,20)#inferior derecha
		aux.line(1184,0,1164,0)
		aux.line(1184,752,1164,752)#superior derecha
		aux.line(1184,752,1184,732)
		axial = [(0,376,20,376),(582,376,602,376),(1184,376,1164,376)]#corte axial
		aux.lines(axial)
		sagital = [(582,752,602,752),(592,752,592,732),(592,376,592,396)]#corte sagital
		aux.lines(sagital)


		#RECUADROS
		aux.setFillColor(sae_blue)
		aux.roundRect(20,20,1144,105,8,stroke = 0, fill = 1)#dibujo el cuadrado inferior
		aux.roundRect(20,395.25,552,105,8,stroke = 0, fill = 1)#dibujo primer cuadro
		aux.roundRect(612,395.25,552,105,8,stroke = 0, fill = 1)#dibujo primer cuadro

		#LINEAS
		aux.setStrokeColor(sae_blue)
		aux.setLineWidth(2)
		aux.setLineCap(1)
		aux.line(20,655,572,655)
		aux.line(612,655,1164,655)
		aux.line(20,250,1164,250)


		#IMAGENES	
		aux.drawImage("sae.png",212,655.50, width= 168, height= 79, mask = None, preserveAspectRatio=True, anchor= 'c')#inserto imagen sae izquierda
		aux.drawImage("sae.png",804,655.50, width= 168, height= 79, mask = None, preserveAspectRatio=True, anchor= 'c')#inserto imagen sae derecha
		aux.drawImage("sae.png",449.75,270, width= 284.50, height= 90.75, mask = None, preserveAspectRatio=True, anchor= 'c')#inserto imagen sae centro

		aux.drawImage("SHCP.png",40,658, width= 125, height= 68, mask = None, preserveAspectRatio=True, anchor= 'c')#inserto imagen shcp izquierda
		aux.drawImage("SHCP.png",632,658, width= 125, height= 68, mask = None, preserveAspectRatio=True, anchor= 'c')#inserto imagen shcp derecha
		aux.drawImage("SHCP.png",60,251, width= 240, height= 123, mask = None, preserveAspectRatio=True, anchor= 'c')#inserto imagen shcp centro

		aux.drawImage("logodoc.png",416,663, width= 120, height= 58, mask = None, preserveAspectRatio=True, anchor= 'c')#inserto imagen doc izquierda
		aux.drawImage("logodoc.png",1014,663, width= 120, height= 58, mask = None, preserveAspectRatio=True, anchor= 'c')#inserto imagen doc derecha
		aux.drawImage("logodoc.png",888,268, width= 255, height= 80, mask = None, preserveAspectRatio=True, anchor= 'c')#inserto imagen doc centro

		#TEXTO Titulos
		aux.setFillColor(navy_blue)#defino el color de la fuente
		aux.setFont('Helvetica-Bold', 30)#defino tipografia y tamaño
		aux.drawCentredString(592,190, str(titulo))
		aux.setFont('Helvetica-Oblique', 20)#defino tipografia y tamaño
		aux.drawCentredString(592,150, str(subtitulo))

		aux.setFont('Helvetica-Bold', 26)#defino tipografia y tamaño
		aux.drawCentredString(296,600, str(titulo))
		aux.setFont('Helvetica-Oblique', 18)#defino tipografia y tamaño
		aux.drawCentredString(296,570, str(subtitulo))

		aux.setFont('Helvetica-Bold', 26)#defino tipografia y tamaño
		aux.drawCentredString(888,600, str(titulo))
		aux.setFont('Helvetica-Oblique', 18)#defino tipografia y tamaño
		aux.drawCentredString(888,570, str(subtitulo))

		#Texto expedientes
		aux.setFillColor("white")#defino el color de la fuente
		aux.setFont('Helvetica-Bold', 40)#defino tipografia y tamaño
		aux.drawCentredString(296,52.5,"Nutras: "+b)#dibujo el texto
		aux.setFont('Helvetica-BoldOblique', 60)#defino tipografia y tamaño
		aux.drawCentredString(900,52.5,"Caja: "+ a + "/" + c)#dibujo el texto

		aux.setFillColor("white")#defino el color de la fuente
		aux.setFont('Helvetica-Bold', 20)#defino tipografia y tamaño
		aux.drawCentredString(148,430,"Nutras: " + b)#dibujo el texto
		aux.setFont('Helvetica-BoldOblique', 42)#defino tipografia y tamaño
		aux.drawCentredString(444,430,"Caja: "+ a + "/" + c)#dibujo el texto

		aux.setFillColor("white")#defino el color de la fuente
		aux.setFont('Helvetica-Bold', 20)#defino tipografia y tamaño
		aux.drawCentredString(740,430,"Nutras: " + b)#dibujo el texto
		aux.setFont('Helvetica-BoldOblique', 42)#defino tipografia y tamaño
		aux.drawCentredString(1036,430,"Caja: "+ a + "/" + c)#dibujo el texto

		aux.showPage()


	aux.save()








	
