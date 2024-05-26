import csv
import re
patron_i = '\('
patron_f = '\)	\d'
libro=open('C:/Users/felip/Documents/libros_pagina_web/LibroMHT2010_sinformato.txt','r')
#indice=open('C:/Users/felip/Documents/libros_pagina_web/indice.txt','w')

with open('C:/Users/felip/Documents/libros_pagina_web/indice.csv', 'w',newline='') as csvfile:
    fieldnames = ['N_cien','N_com1','N_com2','N_com3']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    lineas=libro.readlines()
    for linea in lineas:
    	cadena = linea
    	if (re.search(patron_i, cadena)):
    		if(re.search(patron_f,cadena)):
    			index=re.sub(r'[0-9]+','',cadena)
				index=re.sub(r'	','',index)
				index=index.replace(' (',',(')
				#index=re.sub(r'	\(',',',index)
				indice.write(index)
	indice.close()
	libro.close()


	#writer.writerow('A','B','C','D')
    writer.writerow({'N_cien':'B', 'N_com1': 'Alex', 'N_com2': 'Brian'})
    #writer.writerow({'N_cien': 'A', 'N_com1': 'Rachael','N_com2': 'Rodriguez'})
 
print("Writing complete")