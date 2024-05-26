import pyodbc
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.18.242;DATABASE=SampleDB;UID=sa;PWD=Admin.123')
cursor=conn.cursor()

cliente_id=2
nombre="Juan Palote"
ano_n=1992
email="jp_12mail.cl"
cursor.execute("SET IDENTITY_INSERT clientes ON INSERT INTO clientes (cliente_id,nombre,ano_n,email) VALUES (?,?,?,?)",(cliente_id,nombre,ano_n,email))
conn.commit()
cursor.close()
conn.close()