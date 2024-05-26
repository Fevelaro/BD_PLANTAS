import re
def nombre_comun(strin):
	posicion_f=strin.find(',')
	nc=strin[0:posicion_f]
	nc=re.sub(r'\s','',repr(nc))
	nc=nc.replace('\'','')
	nc=nc.split('/')
	print(type(nc))
	input('pausa')
	return(nc)
resultado=nombre_comun('Abedul (Betula alba)')

for i in resultado:
#	resultado=resultado[i]
	print(i)
	input('pausa')