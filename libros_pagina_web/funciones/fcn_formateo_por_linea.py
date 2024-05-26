import re
def formateo_de_string(cadena):
	patron_i = '\('
	patron_f = '\)	\d'
	if (re.search(patron_i, cadena)):
		if (re.search(patron_f, cadena)): #se busca que en cada linea haya '( ) + digito'
			index=re.sub(r'[0-9]+','',cadena) #se eliminan los digitos que señalan las páginas del libro
			index=re.sub(r'	','',index) # Eliminación de espacios vacíos 1
			index=index.replace(' (',',(')  # Eliminación de espacios vacíos 2
			return(index)
		else:
			return(0)
	else:
		return(0)

resultado=formateo_de_string('Granado / Granada (Punica granatum)	79')
input(resultado)
