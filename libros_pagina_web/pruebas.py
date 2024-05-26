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
	
	for line in planta:
		desc=line.find('Descripción:')
		usom=line.find('Usos medicinales:')
		agro=line.find('Aspectos agronómicos:')
		farma=line.find('Farmacognosia')
		farma=line.find('Farmacodinamia')
		usoc=line.find('Usos comunes:')
		prop=line.find('PROPIEDADES')

		fin=len(line)

		lugares=[desc,usom,agro,farma,usoc,prop,fin]
		input(name)
#		for i in p:
#			if lugares[i] == -1:
#				if i==0:
#					input('Descripción no encontrada')
#				elif i==1:
#					input('Uso medicinal no encontrado')
#				elif i==2:
#					input('Aspectos agronómicos no encontrados')
#				elif i==3:
#					input('Farmacognosis no encontrada')
#				elif i==4:
#					input('Uso común no encontrado')
#				elif i==5:
#					input('Propiedades no encontradas')
#				else:
#					input('error')
#				input(i)
#		input('for de i')
#más abajo hay un error pues no pueden tener igual jerarquia (identación), ya que serían recursivos
#		input(lugares)
		if lugares[0] != -1:
			if lugares[1] !=-1:
				pgdesc=line[desc:usom]
			elif lugares[2] != -1:
				pgdesc=line[desc:agro]
			elif lugares[3] != -1:
				pgdesc=line[desc:farma]
			elif lugares[4] != -1:
				pgdesc=line[desc:usoc]
			elif lugares[5] != -1:
				pgdesc=line[desc:prop]
			elif lugares[6] != -1:
				pgdesc=line[desc:fin]
			input(pgdesc)
			try:
				substr='.'
				res = [i for i in range(len(pgdesc)) if pgdesc.startswith(substr, i)]
			except:
				input('no1')
			input(res)
			try:
				h=pgdesc.find('altura')
				altura=pgdesc[h-22:h+6]
				input(altura)
			except:
				input('no')
#			try:
#				l=pgdesc.find('Hojas')
#				lf=
#				hojas=pgdesc[l-9:l+6]
#				input(altura)
#			except:
#				input('no')


		if lugares[1] != -1:	
			if lugares[2] != -1:
				pgusom=line[usom:agro]
			elif lugares[3] != -1:
				pgusom=line[usom:farma]
			elif lugares[4] != -1:
				pgusom=line[usom:usoc]
			elif lugares[5] != -1:
				pgusom=line[usom:prop]
			elif lugares[6] != -1:
				pgusom=line[usom:fin]

		if lugares[2] != -1:
			if lugares[3] != -1:
				pgagro=line[agro:farma]
			elif lugares[4] != -1:
				pgagro=line[agro:usoc]
			elif lugares[5] != -1:
				pgagro=line[agro:prop]
			elif lugares[6] != -1:
				pgagro=line[agro:fin]


		if lugares[3] != -1:
			if lugares[4] != -1:
				pgfarma=line[farma:usoc]
			elif lugares[5] != -1:
				pgfarma=line[farma:prop]
			elif lugares[6] != -1:
				pgfarma=line[farma:fin]

		if lugares[4] != -1:
			if lugares[5] != -1:
				pgusoc=line[usoc:prop]
			else:
				pgusoc=line[usoc:fin]

		if lugares[5] != -1:
			pgprop=line[prop:fin]


#		lugares.sort()
#		input(lugares)


#		sep=line.find(':')
#		input(sep)
#		input(line)
#		descripcion=line.find('Descripción:')
#		uso=line.find('Usos medicinales:')
#		agro=line.find('Aspectos agronómicos:')
#		farma=line.find('Farmacognosia')
#		input(type(line))
#	escritura=str(dat[int(pg[i]):int(pg[i+1])])
#	planta.write(escritura)