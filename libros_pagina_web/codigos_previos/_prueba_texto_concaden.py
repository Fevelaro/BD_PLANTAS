import csv
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