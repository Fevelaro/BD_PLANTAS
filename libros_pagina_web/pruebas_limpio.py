import csv
import pandas as pd
import numpy as np
urlibro='C:/Users/felip/Documents/libros_pagina_web/LibroMHT2010_sinindice.txt'
urindice='C:/Users/felip/Documents/libros_pagina_web/indice.csv'
pf=6978

dat=[]
libro=open(urlibro,'r')
lineas=libro.readlines()

for linea in lineas:
	dat.append(linea.strip('\n'))

plantas_list=pd.read_csv(urindice)
#input(plantas_list)
n=range(0,103,1)
pg=np.zeros([104,1],dtype=int)

#
#Esta ok el ciclo... pero existen problemas por la variacion que tienen la forma de escribir las plantas.
#COnsiderar además que busca una línea donde slo estén los nombres.
for i in n:
	try:
		pg[i]=dat.index(plantas_list['N_com1'][i])
#		input(pg[i])
	except:
		try:
			pg[i]=dat.index(plantas_list['N_cien'][i])
		except:
			try:
				pg[i]=dat.index(plantas_list['N_com2'][i])
			except:
				try:
					mayus=plantas_list['N_com1'][i].upper()
#					input(mayus)
					pg[i]=dat.index(mayus)
				except:
					try:
						var1=plantas_list['N_com1'][i]+':'
#						input(var1)
						pg[i]=dat.index(var1)
					except:
						try:
							ncom=plantas_list['N_com1'][i]+' / '+plantas_list['N_com2'][i]
#							input(ncom)
							pg[i]=dat.index(ncom)
						except:
							pg[i]=99999
pg[103]=pf
input(pg)
for i in n:
	name=str(plantas_list['N_com1'][i])
	planta=open('C:/Users/felip/Documents/libros_pagina_web/plantas_separadas/'+str(i)+name+'.txt','w')
#	input(type(dat[int(pg[i]):int(pg[i+1])]))
	escritura=str(dat[int(pg[i]):int(pg[i+1])])
	planta.write(escritura)