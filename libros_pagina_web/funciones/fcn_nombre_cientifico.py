#import re
def nombre_cientifico(strin):
	strin=strin.replace(' / ','/')
	strin=strin.replace('( ',',(')  # Eliminación de espacios vacíos antes
	strin=strin.replace(' )',',)')  # Eliminación de espacios vacíos después
	posicion_i=strin.find('(')
	posicion_f=strin.find(')')
	nc=strin[posicion_i+1:posicion_f]
	nc=nc.replace(' ','_')
	nc=nc.replace('/',' o ')
	return(nc)
resultado=nombre_cientifico('a veces me ( gusta milo)')
print(resultado)
input('pausa')