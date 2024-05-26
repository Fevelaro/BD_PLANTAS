import pandas as pd
import re
patron_i = '\('
patron_f = '\)	\d'
libro=open('C:/Users/felip/Documents/libros_pagina_web/LibroMHT2010_sinformato.txt','r')
indice=open('C:/Users/felip/Documents/libros_pagina_web/indice.txt','w')
lineas=libro.readlines()
for linea in lineas:
	cadena=linea
	if (re.search(patron_i, cadena)):
		if (re.search(patron_f, cadena)):
			index=re.sub(r'[0-9]+','',cadena)
			index=re.sub(r'	','',index)
			index=index.replace(' (',',(')
			#index=re.sub(r'	\(',',',index)
			indice.write(index)
indice.close()
libro.close()
#input('pto')
df = pd.read_fwf('C:/Users/felip/Documents/libros_pagina_web/indice.txt')
df.to_csv('C:/Users/felip/Documents/libros_pagina_web/iindce.csv')