#Oracle database

import cx_Oracle  #se importa el modulo para tener acceso a la base de datos oracle
con = cx_Oracle.connect('pythonhol/welcome@127.0.0.1/orcl')
print con.version
con.close()

---------------------------------------------------------------------------------

#MySql Database

import MySQLdb

db = MySQLdb.connect(host="localhost", # tu host, usualmente localhost
                     user="john", # Tu username
                      passwd="megajonhy", # tu contrase;a
                      db="jonhydb") # nombre de la database

# Tienes que crear un objeto Cursor, te va a dejar ejecutar todas las necesidades que necesites
cur = db.cursor() 

# Usa todo el SQL que quieras
cur.execute("SELECT * FROM YOUR_TABLE_NAME")

# Imprime todas las primeras filas de todas las columnas
for row in cur.fetchall() :
    print row[0]

---------------------------------------------------------------------------------

#SQL SERVER


#Instalar el modulo ODBC unixodbc, 
#Modificar /etc/odcinst.ini 
[FreeTDS]
Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so
#Modicar /etc/freetds/freetds.conf
[Global]
TDS_Version = 8.0
client charset = UTF-8
#Importar en el codigo la libreria pypyodbc
import pypyodbc
conn = pypyodbc.connect('Driver=FreeTDS;Server=192.168.1.2;port=1433;uid=sa;pwd=pwd1;database=db_name')
print conn.cursor().execute('select * from a_table').fetchone()[0]
