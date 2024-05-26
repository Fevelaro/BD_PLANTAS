import csv
import re

def nombre_cientifico(strin):
	posicion_i=strin.find('(')
	posicion_f=strin.find(')')
	nc=strin[posicion_i+1:posicion_f]
	return(nc)

patron_i = '\('
patron_f = '\)	\d'
libro=open('C:/Users/felip/Documents/libros_pagina_web/LibroMHT2010_sinformato.txt','r')
indice=open('C:/Users/felip/Documents/libros_pagina_web/indice.txt','w')
n_cien=open('C:/Users/felip/Documents/libros_pagina_web/nombres_cientificos.txt','w')

lineas=libro.readlines()
for linea in lineas:
	cadena=linea
	if (re.search(patron_i, cadena)):
		if (re.search(patron_f, cadena)):
			index=re.sub(r'[0-9]+','',cadena)
			index=re.sub(r'	','',index)
			index=index.replace(' (',',(')
			ncientifico=nombre_cientifico(index)
			n_cien.write('\n'+ncientifico)
			indice.write(index)

indice.close()
libro.close()
n_cien.close()
n_cient=open('C:/Users/felip/Documents/libros_pagina_web/nombres_cientificos.txt', 'r')
csvfile = open('C:/Users/felip/Documents/libros_pagina_web/indice.csv', 'w',newline='')
fieldnames = ['N_cien','N_com1','N_com2','N_com3']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()
	#writer.writerow('A','B','C','D')
lineas=n_cient.readlines()
for linea in lineas:
	writer.writerow({'N_cien':linea})
#writer.writerow({'N_cien':'B', 'N_com1': 'Alex', 'N_com2': 'Brian'})
    #writer.writerow({'N_cien': 'A', 'N_com1': 'Rachael','N_com2': 'Rodriguez'})
 
print("Writing complete")
n_cient.close()
csvfile.close()