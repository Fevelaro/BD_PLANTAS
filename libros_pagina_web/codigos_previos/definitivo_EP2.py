import csv
import re

#función que extrae nombres científicos de una cadena con formato predefinido
def nombre_cientifico(strin):
	strin=strin.replace(' / ','/') # Quita los espacios cuando existe más de un nombre cientifico
	strin=strin.replace('( ',',(')  # Eliminación de espacios vacíos antes
	strin=strin.replace(' )',',)')  # Eliminación de espacios vacíos después
	posicion_i=strin.find('(')
	posicion_f=strin.find(')')
	nc=strin[posicion_i+1:posicion_f] #extrae los nombres científicos de los paréntesis
#	nc=nc.replace(' ','_') #Reemplaza los espacios en blanco dentro de un nombre
	nc=nc.replace('/',' o ') #Separa cuando existe más de un nombre científico para mejorar legibilidad
	return(nc)

#función que extrae los nombre comunes de una cadena con formato predefinido
def nombre_comun(strin):
	posicion_f=strin.find(',')
	nc=strin[0:posicion_f]
	#nc=re.sub(r'\s,',',',repr(nc))
	nc=re.sub(r'\s,\s',',',repr(nc))
	#nc=re.sub(r',\s',',',repr(nc))
	nc=nc.replace('\'','')
	nc=nc.split('/')
#	nc=nc.strip()
	return(nc)
#funcion que toma una línea del libro si pertenece al indice le elimina los espacios vacíos
def formateo_de_string(cadena):
	patron_i = '\('
	patron_f = '\)	\d'
	if (re.search(patron_i, cadena)):
		if (re.search(patron_f, cadena)): #se busca que en cada linea haya '( ) + digito'
			index=re.sub(r'[0-9]+','',cadena) #se eliminan los digitos que señalan las páginas del libro
			index=re.sub(r'	','',index) # Eliminación de espacios vacíos 1
			index=index.replace(' (',',(')  # Eliminación de espacios vacíos 2
			return(index)
		else:
			return(0)
	else:
		return(0)

# Apertura del documento sin formato y creación de archivo csv con cabeceras índice
libro=open('C:/Users/felip/Documents/libros_pagina_web/LibroMHT2010_sinformato.txt','r')#Documento sin formato que contiene todos los datos (en txt)
csvfile = open('C:/Users/felip/Documents/libros_pagina_web/indice.csv', 'w',newline='',encoding='utf-8')#Documento donde se pondran los datos
fieldnames = ['N_cien','N_com1','N_com2','N_com3'] #campos
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()


# Lectura por líneas del libro sin formato
lineas=libro.readlines()

#llamado a funciones para extraer índice y volcarlo en el archivo csv
for linea in lineas:
	caden=linea
	string_formateado=formateo_de_string(caden)
	if string_formateado != 0:
		ncientifico=nombre_cientifico(string_formateado)
		ncomun=nombre_comun(string_formateado)
		if len(ncomun) ==1:
			writer.writerow({'N_com1':ncomun[0],'N_cien':ncientifico})
		if len(ncomun) ==2:
			writer.writerow({'N_com1':ncomun[0],'N_com2':ncomun[1],'N_cien':ncientifico})
		if len(ncomun) ==3:
			writer.writerow({'N_com1':ncomun[0],'N_com2':ncomun[1],'N_cien':ncientifico,'N_com3':ncomun[2]})
csvfile.close()
libro.close()