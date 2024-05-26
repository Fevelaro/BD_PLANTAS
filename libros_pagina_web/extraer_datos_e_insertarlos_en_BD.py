import csv
import re
import pandas as pd
import numpy as np
import os
import pyodbc


absFilePath=os.path.abspath(__file__)
ruta,filename=os.path.split(absFilePath)
rt=ruta
ruta=ruta+'\\plantas_separadas'
files=os.listdir(ruta)
id=-1
for i in range(len(files)):

	ruta_planta=ruta+'\\'+files[i]
	name_planta=ruta_planta.split("\\")
	name_planta=name_planta[len(name_planta)-1]
	for letra in name_planta:
		print(letra)
		if int(letra) == True:
			id=id+int(letra)
			print('entro if')
			input(id)
		else:
			break
	input(id)
#	print(i)
input('fuera for')

print(absFilePath)
print(ruta)
input(files)

#Conectarse a  bd
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.18.242;DATABASE=BD_PLANTAS_2024;UID=sa;PWD=Admin.123')
cursor=conn.cursor()

#estrcuturar el contenido
selva_corpi=str.maketrans({'.':'',"'":'','[':'',']':''})
for i in range(103):
	name=str(plantas_list['N_com1'][i])
	resp=abrir_libro_planta(i,name)
	resp2=resp.split(',')
	caraccon=0
	id_planta=i
	propiedades=''
	for carac in resp2:
		empieza_propiedades=0
		ncomu=resp2[0]
		ncomu=ncomu.translate(selva_corpi)
		caraccon=caraccon+1
		if 'Nombre vernáculo' in carac:
			ncien=resp2[caraccon-2]
			ncien=ncien.translate(selva_corpi)
			ncom='na'
		elif 'Nombres vernáculos' in carac:
			ncien=resp2[caraccon-2]
			ncien=ncien.translate(selva_corpi)
		if 'Descripción: 'in carac:
			empieza_descripcion=caraccon
		if 'Uso popular' in carac:
			termina_descripcion=caraccon
			descripcion=''
			lineas_descripcion=termina_descripcion-empieza_descripcion
			for agrega_descripcion in range(lineas_descripcion-1):
				descripcion=descripcion+resp2[empieza_descripcion+agrega_descripcion]
			descripcion=descripcion.translate(selva_corpi)


		if 'PROPIEDADES' in carac:
			propiedades=''
			empieza_propiedades=caraccon
			lineas_propiedades=len(resp2)-empieza_propiedades
			for agrega_propiedad in range(lineas_propiedades-1):
				propiedades=propiedades+resp2[empieza_propiedades+agrega_propiedad]
			propiedades=propiedades.translate(selva_corpi)
			

	
#	print('id_planta: '+str(i)+'\nNombre científico: '+ncien+'\nNombre Común: '+ncomu+'\nDescripcion: '+descripcion+'\nPropiedades: '+propiedades)	
#	input('for 1 despues')

	cursor.execute("SET IDENTITY_INSERT Planta ON INSERT INTO Planta (id_planta,nombre_cientifico,nombre_comun) VALUES (?,?,?)",(i,ncien,ncomu))



# Confirmar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()
