import csv
import re

#función que extrae nombres científicos de una cadena con formato predefinido
def nombre_cientifico(strin):
	posicion_i=strin.find('(')
	posicion_f=strin.find(')')
	nc=strin[posicion_i+1:posicion_f]
	return(nc)

#función que extrae los nombre comunes de una cadena con formato predefinido
def nombre_comun(strin):
	posicion_f=strin.find(',')
	nc=strin[0:posicion_f]
	nc=re.sub(r'\s','',repr(nc))
	nc=nc.replace('\'','')
	nc=nc.split('/')
	return(nc)

#edición del archivo sin formato para poder trabajarlo, de este:
#se creará un índice que contiene unicamente nombres comunes y científicos
#a dicho índice se le aplica la función y extraen los nombres científicos
#
#criterios para extraer nombres científicos (se eliminan espacios en blanco y conservan paréntesis)
patron_i = '\('
patron_f = '\)	\d'
#Documento sin formato que contiene todos los datos (en txt)
libro=open('C:/Users/felip/Documents/libros_pagina_web/LibroMHT2010_sinformato.txt','r')
#creación de archivo donde se almacenará el indice con nombres comunes y científicos (txt)
indice=open('C:/Users/felip/Documents/libros_pagina_web/indice.txt','w')
#creación de archivo donde se almacenarán los nombres científicos (txt)
n_cien=open('C:/Users/felip/Documents/libros_pagina_web/nombres_cientificos.txt','w')

#edición del archivo base para crear índice(txt)
lineas=libro.readlines()
for linea in lineas:
	cadena=linea
	if (re.search(patron_i, cadena)):
		if (re.search(patron_f, cadena)): #se busca que en cada linea haya '( ) + digito'
			index=re.sub(r'[0-9]+','',cadena) #se eliminan los digitos que señalan las páginas del libro
			index=re.sub(r'	','',index) # Eliminación de espacios vacíos 1
			index=index.replace(' (',',(')  # Eliminación de espacios vacíos 2
			ncientifico=nombre_cientifico(index) #teniendo cada linea formateada se llama a la función que extrae el nombre científico
			n_cien.write('\n'+ncientifico) #se escriben los nombres científicos en el archivo creado con tal fin
			indice.write(index) #se escriben las lineascompletas formateadas en el archivo indice
			nombres_comunes=nombre_comun(index)
indice.close()
libro.close()
n_cien.close()

#Usando el arhivo txt con los nombres científicos se pasan a csv con cabeceras indicando que son nombres científicos
n_cient=open('C:/Users/felip/Documents/libros_pagina_web/nombres_cientificos.txt', 'r')
csvfile = open('C:/Users/felip/Documents/libros_pagina_web/indice.csv', 'w',newline='')
fieldnames = ['N_cien','N_com1','N_com2','N_com3']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()
lineas=n_cient.readlines()
for linea in lineas:
	writer.writerow({'N_cien':linea})
n_cient.close()
csvfile.close()
