#!/usr/bin/env python
# -*- coding: cp1252 -*-

from reportlab.pdfgen import canvas
from reportlab.lib.colors import PCMYKColor

sae_blue = PCMYKColor(62,3.5,23,38)
navy_blue = PCMYKColor(98,5,0,70)

titulo = "Prueba de Supervivencia LyFL 2015-2"
subtitulo = "Marzo 2015"

aux = canvas.Canvas("prueba.pdf")

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
aux.drawCentredString(296,52.5,"Nutras: 000001 - 000002")#dibujo el texto
aux.setFont('Helvetica-BoldOblique', 60)#defino tipografia y tamaño
aux.drawCentredString(900,52.5,"Caja: 1/41")#dibujo el texto

aux.setFillColor("white")#defino el color de la fuente
aux.setFont('Helvetica-Bold', 20)#defino tipografia y tamaño
aux.drawCentredString(148,430,"Nutras: 000001 - 000002")#dibujo el texto
aux.setFont('Helvetica-BoldOblique', 42)#defino tipografia y tamaño
aux.drawCentredString(444,430,"Caja: 1/41")#dibujo el texto

aux.setFillColor("white")#defino el color de la fuente
aux.setFont('Helvetica-Bold', 20)#defino tipografia y tamaño
aux.drawCentredString(740,430,"Nutras: 000001 - 000002")#dibujo el texto
aux.setFont('Helvetica-BoldOblique', 42)#defino tipografia y tamaño
aux.drawCentredString(1036,430,"Caja: 1/41")#dibujo el texto

aux.showPage()


aux.save()
