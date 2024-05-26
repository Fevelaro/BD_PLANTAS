import csv
import pandas as pd
import numpy as np
import re

urindice='C:/Users/felip/Documents/libros_pagina_web/indice.csv'
plantas_list=pd.read_csv(urindice)
n=range(0,103,1)
p=[0,1,2,3,4,5,6]
for i in n:
	name=str(plantas_list['N_com1'][i])
	planta=open('C:/Users/felip/Documents/libros_pagina_web/plantas_separadas/'+str(i)+name+'.txt','r')
	string=planta.read()
	n=string.count("'")
	substr1="'"
	res1 = [i for i in range(len(string)) if string.startswith(substr1, i)]
#	input(res1)
#	if i==102:
#		input('terminamos')
	for j in range(n):
		if j % 2 != 0:
			porcion= string[res1[j-1]+1:res1[j]]
			pos=porcion.find(':')
			especial=string.find('PROPIEDADES')
			input(especial)
			if pos != -1:
				rol=porcion[0:pos]
				info=porcion[pos+2:len(porcion)]
				if rol == 'Descripción':
					print(i,name,rol)
					algo=info
				elif rol == 'Uso popular' or rol=='Usos comunes' or rol=='Usos tradicionales' or rol == 'Uso tradicional':
					alu=info
				elif rol =='Usos medicinales' or rol == 'Uso medicinal':
					print(i,name,rol)
				elif rol=='Farmacodinamia' or rol =='Farmacognosia':
					alf=info
					print(i,name,rol)
				elif rol== 'Recomendaciones':
					alr=info
					print(i,name,rol)
				elif rol == 'Presentación comercial':
					alp=info
					print(i,name,rol)
				elif rol == 'Antecedentes agronómicos':
					alag=info
					print(i,name,rol)
				elif rol=='Efectos':
					ale=info
					print(i,name,rol)
				elif rol == 'Precauciones':
					alp=info
					print(i,name,rol)
				elif rol =='Presentación comercial':
					alpr=info
					print(i,name,rol)
#				elif especial !=-1:
#					resumen=string[especial:len(string)]
#					input(resumen)
#					pass
				else:
					alel=info




				
#				input(info)
#			input(porcion)
#			input(porcion.find(':'))

		else:
			pass


#		input(string(res1[j]))
#		parte=string(j:j+1)
#		try:


#	substr=':'
#	res = [i for i in range(len(string)) if string.startswith(substr, i)]
	
	#for n in res:
	#	input(string[n-10:n])
	#input(res)