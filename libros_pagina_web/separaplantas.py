import csv
import pandas as pd
def separa(libro,urindice):
	dat=[]
	separados=[]
	libro=open(urlibro,'r')
	lineas=libro.readlines()
	for linea in lineas:
		dat.append(linea.strip('\n'))
	
	plantas_list=pd.read_csv(urindice)
	#numero_de_filas=plantas_list.shape[0]-1
	for i in plantas_list["N_cien"].index:
		separados[i]=dat[dat.index(plantas_list["N_cien"][i]):dat.index(plantas_list["N_cien"][i+1])]
		print(plantas_list["N_cien"][i])
		input('ji')
	input(separados)

urlibro='C:/Users/felip/Documents/libros_pagina_web/LibroMHT2010_sinindice.txt'
urindice='C:/Users/felip/Documents/libros_pagina_web/indice.csv'
separa(urlibro,urindice)
