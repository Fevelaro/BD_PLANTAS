import csv
import pandas as pd
import numpy as np
import re

urindice='C:/Users/felip/Documents/libros_pagina_web/indice.csv'
plantas_list=pd.read_csv(urindice)
for i in range(103):
	name=str(plantas_list['N_com1'][i])
	planta=open('C:/Users/felip/Documents/libros_pagina_web/plantas_separadas/'+str(i)+name+'.txt','r')
	string=planta.read()
	propiedades=string[string.find('PROPIEDADES'):len(string)]
	string=string[0:string.find('PROPIEDADES')-1]
	substr1="'"
	res1 = [i for i in range(len(string)) if string.startswith(substr1, i)]
	input(res1)
	input(range(len(res1)))
	trozo=[a for i in range(len(res1)) ]#a=string[res1[i]:res1[i+1]]]
	input(trozo)
	