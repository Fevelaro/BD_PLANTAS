import csv
import re
import pandas as pd
import numpy as np
import os
import pyodbc
#función que separa las plantas y las guarda como libros separados en una carpeta especial
def separa_plantas(urlibro,urindice,pf):
	pf=int(pf)
	dat=[]
	libro=open(urlibro,'r')
	lineas=libro.readlines()
	for linea in lineas:
		dat.append(linea.strip('\n'))
	plantas_list=pd.read_csv(urindice)
	n=range(0,103,1)
	pg=np.zeros([104,1],dtype=int)
	for i in n:
		try:
			pg[i]=dat.index(plantas_list['N_com1'][i])
		except:
			try:
				pg[i]=dat.index(plantas_list['N_cien'][i])
			except:
				try:
					pg[i]=dat.index(plantas_list['N_com2'][i])
				except:
					try:
						mayus=plantas_list['N_com1'][i].upper()
						pg[i]=dat.index(mayus)
					except:
						try:
							var1=plantas_list['N_com1'][i]+':'
							pg[i]=dat.index(var1)
						except:
							try:
								ncom=plantas_list['N_com1'][i]+' / '+plantas_list['N_com2'][i]
								pg[i]=dat.index(ncom)
							except:
								pg[i]=99999
	pg[103]=pf
	for i in n:
		name=str(plantas_list['N_com1'][i])		
		planta=open('C:/Users/felip/Documents/libros_pagina_web/plantas_separadas/'+str(i)+name+'.txt','w')
		escritura=str(dat[int(pg[i]):int(pg[i+1])])
		planta.write(escritura)
	return()

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
##recibe el nombre y busca dentro de la info de la planta
def abrir_libro_planta(i,name):
	planta=open('C:/Users/felip/Documents/libros_pagina_web/plantas_separadas/'+str(i)+name+'.txt','r')
	string=planta.read()
#	print(string)
#	print('abrir libro plata')
	return(string)
##Extraer info de libro
def extraccion_info(string):
	info_planta=[[],[],[],[]]
#	propiedades=string[string.find('PROPIEDADES'):len(string)]
#	input(propiedades)
	info_planta[0]=propiedades
	string=string[0:string.find('PROPIEDADES')-1]
	substr1="'"
	res1 = [k for k in range(len(string)) if string.startswith(substr1, k)]
	for j in range(len(res1)):
		if j %2 != 0:
			tramo=string[res1[j-1]+1:res1[j]]
			rol=tramo[0:tramo.find(':')]
			info=tramo[tramo.find(':')+1:len(tramo)]
			if rol=='Descripción':
				#input('1')
				info_planta[1]=info
				#writer.writerow({'ID':[i],'Nombre':name,'Descripción':info})
			elif rol == 'Uso popular' or rol=='Usos comunes' or rol=='Usos tradicionales' or rol == 'Uso tradicional':
				#input('2')
				info_planta[2]=info
				#writer.writerow({'ID':[i],'Nombre':name,'Uso':info})
			elif rol =='Usos medicinales' or rol == 'Uso medicinal':
				#input('3')
				info_planta[3]=info
				#writer.writerow({'ID':[i],'Nombre':name,'Uso':info})
			elif rol=='Farmacodinamia' or rol =='Farmacognosia':
				#input('4')
				info_planta[4]=info
				#writer.writerow({'ID':[i],'Nombre':name,'Farmacodinamia':info})
			elif rol== 'Recomendaciones':
				#input('5')
				info_planta[5]=info
				#writer.writerow({'ID':[i],'Nombre':name,'Recomendaciones':info})
			elif rol == 'Presentación comercial':
				#input('6')
				info_planta[6]=info
				#writer.writerow({'ID':[i],'Nombre':name,'Presentación':info})
			elif rol == 'Antecedentes agronómicos':
				#input('7')
				info_planta[7]=info
				#writer.writerow({'ID':[i],'Nombre':name,'Antecedentes':info})
			elif rol=='Efectos':
				#input('8')
				info_planta[8]=info
				#writer.writerow({'ID':[i],'Nombre':name,'Efectos':info})
			elif rol == 'Precauciones':
				#input('9')
				info_planta[9]=info
				#writer.writerow({'ID':[i],'Nombre':name,'Precauciones':info})
	return(info_planta)

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
##LLamado a función separa plantas
urlibro='C:/Users/felip/Documents/libros_pagina_web/LibroMHT2010_sinindice.txt'
urindice='C:/Users/felip/Documents/libros_pagina_web/indice.csv'
pf=6978
separa_plantas(urlibro,urindice,pf)
plantas_list=pd.read_csv(urindice)
datos=[]
csv_file_info = open('C:/Users/felip/Documents/libros_pagina_web/informacion.csv', 'w',newline='',encoding='utf-8')#Documento donde se pondran los datos

#Conectarse a  bd
#conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.18.242;DATABASE=BD_PLANTAS_2024;UID=sa;PWD=Admin.123')
#cursor=conn.cursor()
#num0=0

#estrcuturar el contenido
selva_corpi=str.maketrans({'.':'',"'":'','[':'',']':''})
for i in range(103):
	name=str(plantas_list['N_com1'][i])
	resp=abrir_libro_planta(i,name)
	resp2=resp.split(',')
	caraccon=0
	id_planta=i
	propiedades=''
	for carac in resp2:
		empieza_propiedades=0
		ncomu=resp2[0]
		ncomu=ncomu.translate(selva_corpi)
		caraccon=caraccon+1
		if 'Nombre vernáculo' in carac:
			ncien=resp2[caraccon-2]
			ncien=ncien.translate(selva_corpi)
			ncom='na'
		elif 'Nombres vernáculos' in carac:
			ncien=resp2[caraccon-2]
			ncien=ncien.translate(selva_corpi)
		if 'Descripción: 'in carac:
			empieza_descripcion=caraccon
		if 'Uso popular' in carac:
			termina_descripcion=caraccon
			descripcion=''
			lineas_descripcion=termina_descripcion-empieza_descripcion
			for agrega_descripcion in range(lineas_descripcion-1):
				descripcion=descripcion+resp2[empieza_descripcion+agrega_descripcion]
			descripcion=descripcion.translate(selva_corpi)


		if 'PROPIEDADES' in carac:
			propiedades=''
			empieza_propiedades=caraccon
			lineas_propiedades=len(resp2)-empieza_propiedades
			for agrega_propiedad in range(lineas_propiedades-1):
				propiedades=propiedades+resp2[empieza_propiedades+agrega_propiedad]
			propiedades=propiedades.translate(selva_corpi)
	if 'efectos' in propiedades or 'Efectos' in propiedades:
	#	print('efectos')
		print(ncomu)
	#if 'diabetes' in propiedades:
	#	print('diabetes')
	#if 'tensión' in propiedades:
	#	print('presión')
	#if 'febri' in propiedades:
	#	print('fiebre')
	coleretica antihelmíntica antibacteriana emenagogo vermifugo
			
	#print(propiedades)
	#input('panta')
	
	#print('id_planta: '+str(i)+'\nNombre científico: '+ncien+'\nNombre Común: '+ncomu+'\nDescripcion: '+descripcion+'\nPropiedades: '+propiedades)	
#	if 'tensión' in propiedades:
#		print(ncomu)


	#cursor.execute("SET IDENTITY_INSERT Planta ON INSERT INTO Planta (id_planta,nombre_cientifico,nombre_comun,propiedades) VALUES (?,?,?,?)",(i,ncien,ncomu,propiedades))



# Confirmar los cambios
#conn.commit()

# Cerrar la conexión
#cursor.close()
#conn.close()
